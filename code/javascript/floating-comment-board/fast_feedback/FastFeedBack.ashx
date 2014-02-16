<%@ WebHandler Language="C#" Class="FastFeedback" %>

using System;
using System.Web;

public class FastFeedback : IHttpHandler, System.Web.SessionState.IRequiresSessionState
{
    //最终状态
    public enum FeedbackState
    {
        UniqueCodeError = 1,
        Succeed = 5,
        Error = 10,
        Null = 20
    }
    
    public void ProcessRequest (HttpContext context) {
        context.Response.ContentType = "text/plain";
        context.Response.CacheControl = "no-cache"; //清空缓存
        
        string code = context.Request["SecurityCode"];
        string message = context.Request["Message"];

        if (string.IsNullOrEmpty(code) || string.IsNullOrEmpty(message))
        {
            context.Response.Write(FeedbackState.Null.ToString());
            context.Response.End();
            return; 
        }

        try
        {
            if (code.ToUpper() == context.Session["ImageUniqueCode"].ToString())
            {
                //执行成功,完成其他任务
                //....do.....
                context.Response.Write(FeedbackState.Succeed.ToString());

            }
            else
            {
                context.Response.Write(FeedbackState.UniqueCodeError.ToString());

            }
        }
        catch (Exception ex)
        {
            context.Response.Write(FeedbackState.Error.ToString());
        }
        finally
        {
            context.Response.End(); 
        }
    }
 
    public bool IsReusable {
        get {
            return false;
        }
    }

}