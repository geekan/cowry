# Modify the jpg input, take the result.

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

def nms_detections(dets, overlap=0.3):
    """
    Non-maximum suppression: Greedily select high-scoring detections and
    skip detections that are significantly covered by a previously
    selected detection.

    This version is translated from Matlab code by Tomasz Malisiewicz,
    who sped up Pedro Felzenszwalb's code.

    Parameters
    ----------
    dets: ndarray
        each row is ['xmin', 'ymin', 'xmax', 'ymax', 'score']
    overlap: float
        minimum overlap ratio (0.3 default)

    Output
    ------
    dets: ndarray
        remaining after suppression.
    """
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    ind = np.argsort(dets[:, 4])

    w = x2 - x1
    h = y2 - y1
    area = (w * h).astype(float)

    pick = []
    while len(ind) > 0:
        i = ind[-1]
        pick.append(i)
        ind = ind[:-1]

        xx1 = np.maximum(x1[i], x1[ind])
        yy1 = np.maximum(y1[i], y1[ind])
        xx2 = np.minimum(x2[i], x2[ind])
        yy2 = np.minimum(y2[i], y2[ind])

        w = np.maximum(0., xx2 - xx1)
        h = np.maximum(0., yy2 - yy1)

        wh = w * h
        o = wh / (area[i] + area[ind] - wh)

        ind = ind[np.nonzero(o <= overlap)[0]]

    return dets[pick, :]

def plot_patch(det_name, colors, df, predictions_df):
    scores = predictions_df[det_name]
    windows = df[['xmin', 'ymin', 'xmax', 'ymax']].values
    dets = np.hstack((windows, scores[:, np.newaxis]))
    nms_dets = nms_detections(dets)

    currentAxis = plt.gca()
    for c, det in zip(colors, nms_dets[:len(colors)]):
        if det[4] < 0:
            break
        plt.text(det[0], (det[3]-det[1])*10/10+det[1],
                 str(det[4])+'\n'+det_name,
                 bbox=dict(facecolor='white', alpha=0.5))
        currentAxis.add_patch(
            plt.Rectangle((det[0], det[1]), det[2]-det[0], det[3]-det[1],
            fill=False, edgecolor=c, linewidth=5)
        )
    print 'scores:', nms_dets[:len(colors), 4]

def detect_img(img_name):
    os.system("mkdir -p _temp")
    os.system("echo `pwd`/"+img_name+" > _temp/det_input.txt")
    os.system("echo `pwd`")
    os.system("../python/detect.py --crop_mode=selective_search \
      --pretrained_model=/Users/wuchenglin/git/caffe/models/bvlc_reference_rcnn_ilsvrc13/bvlc_reference_rcnn_ilsvrc13.caffemodel \
      --model_def=/Users/wuchenglin/git/caffe/models/bvlc_reference_rcnn_ilsvrc13/deploy.prototxt \
      --raw_scale=255 _temp/det_input.txt _temp/det_output.h5 > detect.log 2>&1")

    print('')
    df = pd.read_hdf('_temp/det_output.h5', 'df')
    print(df.shape)
    print(df.iloc[0])

    with open('../data/ilsvrc12/det_synset_words.txt') as f:
        labels_df = pd.DataFrame([
            {
                'synset_id': l.strip().split(' ')[0],
                'name': ' '.join(l.strip().split(' ')[1:]).split(',')[0]
            }
            for l in f.readlines()
        ])
    labels_df.sort('synset_id')
    predictions_df = pd.DataFrame(np.vstack(df.prediction.values), columns=labels_df['name'])
    # print(predictions_df.iloc[0])

    max_s = predictions_df.max(0)
    max_s.sort(ascending=False)
    print(max_s[:10])

    det_name = max_s.index[0]

    im = plt.imread(img_name)
    plt.imshow(im)
    colors = ['r', 'b', 'y']

    for index, i in enumerate(max_s):
        if i > 0:
            print "plot_patch", index, i, max_s.index[index]
            plot_patch(max_s.index[index], colors, df, predictions_df)
            plt.savefig('out/'+img_name)
        else:
            break
    # plot_patch(plt, det_name, colors, df, predictions_df)
    return

def main():
    img_name = 'images/ilsvrc2011/1.n00004475_15899.2875184020_9944005d0d.jpg'
    detect_img(img_name)

if __name__ == '__main__':
    main()
