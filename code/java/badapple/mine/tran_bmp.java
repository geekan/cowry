package badapple_minesweeperver;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;

public class tran_bmp {
	
	//图像建议压缩到80x60
	public static double gamma=2;
	public static double whitepoint=0.666667;
	public static double blackpoint=0.333333;
	public static int headlong=57;
	public static String fileroot="Z:/TEM/";
	
	
	public static int [][][] imagemap;
	public static int [][][] imagetarget;
	public static int [][]colorpanelin16bit=new int [16][4];
	public static int [][][] iconmap=new int [16][16][16];
	
	//0、头大小、1、宽、2、高、3、位平面、4、色位
	public static int []imageinfo=new int [5];
	
	public static void main(String[] args) {
		
		
		for(int i=1;i<2;i++)
		{
			StringBuffer sb=new StringBuffer(fileroot);
			sb=sb.append(String.format("%06d", i));
			String filepathi=sb.append(".bmp").toString();
			String filepatho=sb.append(".txt").toString();
			readfile(filepathi);
			readimage(filepathi);
			tran_to_math();
			System.out.println(imageinfo[4]);
			if(imageinfo[4]!=32)geticon();
			else 
				checkmine();
			writefile(filepatho);
		}
	}
	/*先做一个文本文件写入,姑且用于方便后期读写*/
	public static void writefile(String filepatho)
	{
		try {
			File fileo=new File(filepatho);
			fileo.createNewFile();
			BufferedWriter bw=new BufferedWriter(new FileWriter(new File(filepatho)));
			//先写雷的色板和点阵
			if(imageinfo[4]==4)
			{
				String colourpanel=filepatho+".clp.txt";
				BufferedWriter cp=new BufferedWriter(new FileWriter(new File(colourpanel)));
				for(int i1=0;i1<16;i1++)
				{
					for(int i2=0;i2<4;i2++)
					{
						cp.write(Integer.toString(colorpanelin16bit[i1][i2]));
						if (i2<3) cp.write("\t");
					}
					cp.newLine();
				}
				cp.flush();
				cp.close();
				for(int i1=0;i1<iconmap.length;i1++)
				{
					for(int i2=0;i2<iconmap[0].length;i2++)
					{
						for(int i3=0;i3<iconmap[0][0].length;i3++)
						{
							bw.write(Integer.toString(iconmap[i1][i2][i3]));
							if(i3<iconmap[0][0].length-1) bw.write("\t");
						}
						bw.newLine();
					}
				}
				bw.flush();
				bw.close();
			}
			else
				if(imageinfo[4]==32)
				{
					for(int i1=0;i1<imagemap.length;i1++)
					{
						for(int i2=0;i2<imagemap[0].length;i2++)
						{
							bw.write(Integer.toString(imagemap[i1][i2][0]));
							if(i2<imagemap[0].length-1) bw.write("\t");
						}
						bw.newLine();
					}
					bw.flush();
					bw.close();
				}
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	/*填充雷的数量*/
	public static void checkmine()
	{	/*图片的-1为白,-2灰,-3黑,暂定灰白加入计算,黑为雷*/
		int imagehigh=imagemap.length;
		int imagewide=imagemap[0].length;
		for(int i1=0;i1<imagehigh;i1++)
		{
			for(int i2=0;i2<imagewide;i2++)
			{
				if(imagemap[i1][i2][0]!=-3)
				{
					int c=checkminecell(i1,i2);
					if(c>0)imagemap[i1][i2][0]=c;
				}
				//System.out.print(imagemap[i1][i2][0]+"\t");
			}
			//System.out.println();
		}
	}
	public static int checkminecell(int y,int x)
	{
		int imagehigh=imagemap.length;
		int imagewide=imagemap[0].length;
		int count=0;
		for(int i1=y-1;i1<=y+1;i1++)
			for(int i2=x-1;i2<=x+1;i2++)
			{
				if(i1>0&&i2>0&&i1<imagehigh&&i2<imagewide)
				{
					if(imagemap[i1][i2][0]==-3)count++;
				}
			}
		return count;
	}
	
	
	/*获取扫雷的图标文件,每个16x16*/
	public static void geticon()
	{
		for(int i1=0;i1<16;i1++)
		{
			for(int i2=0;i2<16;i2++)
			{
				for(int i3=0;i3<16;i3++)
				{
					iconmap[i1][i2][i3]=imagemap[i2+i1*16][i3][0];
					//System.out.printf("%3s",Integer.toHexString(iconmap[i1][i2][i3]));
				}
				//System.out.println();
			}
			//System.out.println();
			//System.out.println();
		}
			
	}
	
	/*********************************下面是普通的读取,上面开始转换到输出部分*/
	
	/*将图片转换为数字*/
	/*图片的-1为白,-2灰,-3黑*/
	public static void tran_to_math()
	{
		int imagehigh=imagemap.length;
		int imagewide=imagemap[0].length;
		int bitdep=imageinfo[4];
		double gammapoint0=Math.pow(blackpoint, gamma);
		double gammapoint1=Math.pow(whitepoint, gamma);

		//System.out.println("imagewide="+imagewide);
		//System.out.println("imagehigh="+imagehigh);
		if(bitdep!=4)
		{
			//System.out.println("gammapoint0="+256*gammapoint0);
			//System.out.println("gammapoint1="+256*gammapoint1);
			for(int i1=0;i1<imagehigh;i1++)
			{
				for(int i2=0;i2<imagewide;i2++)
				{	//System.out.print(imagemap[i1][i2][0]);
					if(imagemap[i1][i2][0]>256*gammapoint1)
					{
						imagemap[i1][i2][0]=-1;
						//System.out.print("■");
					}
					else if (imagemap[i1][i2][0]>256*gammapoint0)
					{
						imagemap[i1][i2][0]=-2;
						//System.out.print("┼");
					}
					else 
					{
						imagemap[i1][i2][0]=-3;
						//System.out.print("□");
					}
				}
				//System.out.println();
			}
		}
		else
		{/*
			for(int i1=0;i1<imagehigh;i1++)
			{
				for(int i2=0;i2<imagewide;i2++)
				{	
					switch (imagemap[i1][i2][0]) {
					case 0:	System.out.print("□");	break;
					case 1:	System.out.print("┼");	break;
					case 2:	System.out.print("╋");	break;
					case 3:	System.out.print("□");	break;
					case 4:	System.out.print("〓");	break;
					case 5:	System.out.print("★");	break;
					case 6:	System.out.print("☆");	break;
					case 7:	System.out.print("○");	break;
					case 8:	System.out.print("●");	break;
					case 9:	System.out.print("◆");	break;
					case 10:System.out.print("◇");	break;
					case 11:System.out.print("▲");	break;
					case 12:System.out.print("△");	break;
					case 13:System.out.print("∵");	break;
					case 14:System.out.print("＃");	break;
					case 15:System.out.print("■");	break;
					default:	break;
					}
				}
				System.out.println();
			}*/
		}
		
	}
	/*读取图像*/
	public static void readimage(String filepath)
	{
		try {
		File file=new File(filepath);
		FileInputStream filein;
		filein = new FileInputStream(file);
		int imagewide=imageinfo[1];
		int imagehigh=imageinfo[2];
		//预读取
		
	
		//System.out.println("singlepixel len="+((Math.log(imageinfo[4])/Math.log(2))-2));
		//System.out.println("singlepixel len v2="+imageinfo[4]/8);
		
		/*读取数据,并将负数重新转正*/
		byte []singlepixe;
		if(imageinfo[4]/8>0)
		{singlepixe=new byte[imageinfo[4]/8];}
		else{singlepixe=new byte[1];}
		
		/*24位色(实标32位)*/
		if(imageinfo[4]/8!=0)
		{	
			byte[] filehead=new byte[imageinfo[0]+3];
			filein.read(filehead);
			for(int i1=0;i1<imagehigh;i1++)
			{
				//System.out.print((countline++)+"\t");
				for(int i2=0;i2<imagewide;i2++)
				{
					filein.read(singlepixe);
					{
						for(int i3=0;i3<singlepixe.length;i3++)
						{
							if(singlepixe[i3]<0)imagemap[i1][i2][i3]=singlepixe[i3]+256;
							else imagemap[i1][i2][i3]=singlepixe[i3];
						}
					}
					//System.out.println();
				}
			}
			int ave;
			//System.out.println("here");
			for(int i1=0;i1<imagehigh;i1++)
			{
				for(int i2=0;i2<imagewide;i2++)
				{
					ave=0;
					for(int i3=1;i3<4;i3++)
					{
						ave+=imagemap[i1][i2][i3];
					}
					imagemap[i1][i2][0]=ave/3;
					//System.out.print(imagemap[i1][i2][0]+"\t");
				}
				//System.out.println();
			}
		}
		else
			/*16色处理,先取出色版,再取出*/
		{
			/*取文件头*/
			byte[] filehead=new byte[imageinfo[0]-65];
			filein.read(filehead);/*
			for(int i1=0;i1<filehead.length;i1++)
			{
				System.out.printf("%3d",i1);
			}
			System.out.println();
			for(int i1=0;i1<filehead.length;i1++)
			{
				System.out.printf("%3d",filehead[i1]);
			}
			System.out.println();*/
			/*取色板*/
			byte[] colorpanel=new byte[65];
			filein.read(colorpanel);
			/*
			System.out.println("colorpanel.length="+colorpanel.length);
			for(int i1=0;i1<colorpanel.length;i1++)
			{
				System.out.printf("%3d",i1);
			}
			System.out.println();
			*/
			for(int i1=0;i1<64;i1+=4)
			{
				for(int i2=0;i2<4;i2++)
				{
					if(colorpanel[i1+i2]<0) colorpanelin16bit[i1/4][i2]=colorpanel[i1+i2]+256;
					else colorpanelin16bit[i1/4][i2]=colorpanel[i1+i2];
					//System.out.printf("%3s",Integer.toHexString(colorpanelin16bit[i1/4][i2]));
				}
				//System.out.println();
			}
			//System.out.println();
			
			/*取色*/
			int []lowbitread=new int [imagehigh*imagewide];
			for(int i1=0;i1<imagehigh*imagewide;i1+=2)
			{
				filein.read(singlepixe);
				int temp;
				if(singlepixe[0]<0)temp=singlepixe[0]+256;
				else temp=singlepixe[0];
				lowbitread[i1]=temp/16;
				lowbitread[i1+1]=temp%16;
			}
			for(int i1=0;i1<imagehigh;i1++)
			{
				for(int i2=0;i2<imagewide;i2++)
				{
					imagemap[i1][i2][0]=lowbitread[i1*imagewide+i2];
					//System.out.print(Integer.toHexString(imagemap[i1][i2][0]));
				}
				//System.out.println();
			}
		}
		filein.close();
		/*求取平均值/调色*/
		
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	public static void readfile(String filepath)
	{
		try {
			int imagewide=0;
			int imagehigh=0;
			//System.out.println(filepath);
			File file=new File(filepath);
			FileInputStream filein=new FileInputStream(file);
			//System.out.println(file.canWrite());
			//57
			byte[] filehead=new byte[headlong];
			filein.read(filehead, 0, headlong);
			int[] filehead2=new int[headlong];
			for(int i=0;i<filehead.length;i++)
			{
				//System.out.print(Integer.toHexString(filehead[i])+" ");
				if(filehead[i]<0)filehead2[i]=filehead[i]+256;
				else filehead2[i]=filehead[i];
			}
			
			
			/*输出图片文件的头部，测试用*/
			/*
			for(int i=0;i<filehead.length;i++)
			{
				System.out.printf("%3d ",i);
			}
			System.out.println();
			for(int i=0;i<filehead.length;i++)
				{
				System.out.printf("%3s ",Integer.toHexString(filehead2[i]));
				//System.out.print(filehead2[i]+" ");
			}
			System.out.println();
			*/
			
			/*计算图像的长宽*/
			/*10为头大小，18-20为宽度，22-24为高度，*/
			for(int i=0;i<3;i++)
			{
				imagewide+=filehead2[20-i]*Math.pow(16, 2-i)*Math.pow(16, 2-i);
				imagehigh+=filehead2[24-i]*Math.pow(16, 2-i)*Math.pow(16, 2-i);
			}
			
			/*输出一些参数*/
			//System.out.println("imagewide="+imagewide);
			//System.out.println("imagehigh="+imagehigh);
			imagemap=new int [imagehigh][imagewide][4];
			//System.out.println("headlenth="+filehead2[10]);
			//System.out.println("bitdepth="+filehead2[28]);
			imageinfo[0]=filehead2[10];
			imageinfo[1]=imagewide;
			imageinfo[2]=imagehigh;
			imageinfo[3]=1;
			imageinfo[4]=filehead2[28];

			filein.close();
		} catch (FileNotFoundException e) {	
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}

}
