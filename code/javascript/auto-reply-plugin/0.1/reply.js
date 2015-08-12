var pattern = /<script\s+[^>]*>replyreload.*<\/script>/;
var html = document.documentElement.innerHTML;
var find = html.match(pattern);
if(find)
{
	var fp_msg = document.getElementById('fastpostmessage');
	var fp_button = document.getElementById('fastpostsubmit');
	var fp_refresh = document.getElementById('fastpostrefresh');
	if(fp_msg && fp_button)
	{
		msg = "hmm 让我思考一下够不够字数";
		if(fp_refresh)
		{
			tmp = fp_refresh.checked;
			fp_refresh.checked = false;
		}
		fp_msg.innerText = msg;
		fp_button.click();
		fp_refresh.checked = tmp;
	}
}
