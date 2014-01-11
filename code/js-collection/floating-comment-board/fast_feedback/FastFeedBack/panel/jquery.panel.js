/// <reference name="MicrosoftAjax.js"/>
/*!
*   My Feedback(Jquery Plugin)
*
* Copyright (c) 2009 Andy Huang
* Date: Sunday, February 01, 2009
* Version: V1.0
*/
(function($) {
    //浮动层开始-----------------
    $.fn.panel = function(options) {
        //获取传入的参数
        var opts = $.extend({}, $.fn.panel.defaults, options);
        var ie6 = false; //判断ie6
        if ($.browser.msie && jQuery.browser.version < 7) {
            ie6 = true;
            try {
                document.execCommand("BackgroundImageCache", false, true);
            } catch (err) { }
        }
        //执行
        return this.each(function() {
            $this = $(this); //全局对象,整个浮动层
            var o = $.meta ? $.extend({}, opts, $this.data()) : opts;
            //层定位,可改写你喜欢定位的位置(结合scroll()事件)
            var loc = { right: o.right + "px", bottom: o.bottom + "px" };
            $this.css({ "z-index": "9999", "position": "fixed" }).css(loc);
            //解决ie6 层定位的bug
            if (ie6) {
                resize(); //位置
                scroll(); // 滚动
            }

            //创建留言板和绑定事件
            createDiv();
            bindButtonEvent();

        });
    };
    function resize() {
        $(window).resize(function() {
            ie6style();
        });
    }
    function scroll() {
        $this.css("position", "absolute");
        $(window).scroll(function() {
            ie6style();
        });
    }
    function ie6style() {
        $(window).scroll(function() {
            //unkown code,who can help me?
            $this.css({ "bottom": "0px" });
            $this.css({ "right": "0px", "bottom": "1px" });
        });
    }
    //浮动层结束------------------

    //留言板
    function createDiv() {
        var obj = $.fn.panel.defaults;
        // create message title
        var str = "<div id='jquery_panel_title' class='jquery_panel_title'><div class='title_font'>" + $.fn.panel.defaults.title + "<span class='jquery_message_num'></span></div>";
        str += "<div class='jquery_panel_button'>";
        str += "<label id='jquery-x-tool-close' class='jquery-x-tool close' title=''></label>";
        str += "<label id='jquery-x-tool-down' class='jquery-x-tool down' title=''></label>";
        str += "</div></div>";
        // create message body
        str += "<div id='jquery_panel_message' class='jquery_panel_message'>";
        str += "<center>";
        str += "<div class='jquery_message_tip' style='display:none'>" + obj.messagetip + "</div>";
        str += "<div class='jquery_panel_messagebox'><textarea id='jquery_panel_txtmessagebox' class='min' >" + obj.messagebox + "</textarea></div>";
        str += "<div class='jquery_panel_code' style='display:none;'>Security Code:<input id='jquery_panel_txtcode' type='text' maxlength='4' />&nbsp;<iframe src='" + obj.scurityuniquecodeurl + "' class='jquery_scuritycode' frameborder='0' scrolling='no' marginwidth='0' marginheight='0' /></iframe><span class='jquery_scuritycode_submit'>Try a different image</span></div>"
        str += "<div class='jquery_panel_error' style='display: none'></div>";
        str += "<div class='jquery_panel_submit' style='display: none'><input id='jquery_panel_submit' type='button' value='Submit' /></div>";
        str += "</center></div>";
        $this.append(str);
    }
    //留言板事件
    function bindButtonEvent() {
        var obj = $.fn.panel.defaults;
        var messagebox = $("#jquery_panel_txtmessagebox");  //消息框
        var messagecount = $(".jquery_message_num");        //消息框字符统计
        var error = $(".jquery_panel_error");               //错误层 
        var ucode = $(".jquery_panel_code");                //安全码层
        var codebox = $("#jquery_panel_txtcode");           //安全码框
        var submit = $(".jquery_panel_submit");             //确认按钮层

        //刷新验证码
        $(".jquery_scuritycode_submit").click(function() {
            $(".jquery_scuritycode").each(function() {
                this.contentWindow.location.reload(); // opera 9 不支持,其它都正常
            });
        });

        //关闭按钮事件
        $("#jquery-x-tool-close").click(function() {
            $this.hide();
        });

        //down/up button
        $("#jquery-x-tool-down").click(function() {
            var msg = $("#jquery_panel_message");
            if (msg.css("display") == "block") {
                msg.slideUp(200);
                $(this).removeClass("down").addClass("up");
                messagebox.removeClass("max").addClass("min");
                submit.hide();
                ucode.hide();
                error.hide();
                $this.css("width", "180px"); // 缩小后大小,于css设置要一致
            }
            else {
                msg.slideDown();
                $(this).removeClass("up").addClass("down");
            }

        });
        //文本框焦点事件
        messagebox.focus(function() {
            if ($(this).val() == obj.messagebox) {
                $(this).val("").empty();
            }
            $this.css("width", "470px"); // 放大后大小,于css设置要一致
            $(this).addClass("max");
            submit.show();
            ucode.show();
        }).addClass("inputnormal").keyup(function() {
            var msg = $.trim(messagebox.val());
            messagecount.empty().append("(" + msg.length + ")");
            if (msg.length >= 20 && msg.length <= 1000) {
                messagebox.removeClass("inputerror").addClass("inputnormal");
            }
        });
        //验证码样式
        codebox.addClass("inputnormal").keyup(function() {
            if (codebox.val().length == 4) {
                $(this).removeClass("inputerror").addClass("inputnormal");
            }
        });

        //确认按钮事件
        $("#jquery_panel_submit").click(function() {
            var msg = $.trim(messagebox.val());
            if (msg.length < 20 || msg.length > 1000) {
                error.show().text(obj.messageboxerror);
                messagebox.removeClass("inputnormal").addClass("inputerror");
            }
            else if (codebox.val().length == 0) {
                error.show().text(obj.scurityuniquecodeerror);
                codebox.focus().removeClass("inputnormal").addClass("inputerror");
            }
            else {
                error.hide();
                sendmessage(); //完成后发送到服务器事件
            }
        });

    }
    //服务器xmlhttp request事件
    function sendmessage() {
        var message = $("#jquery_panel_txtmessagebox"); //消息框
        var codebox = $("#jquery_panel_txtcode");       //安全码框
        var btn = $("#jquery_panel_submit");            //确认按钮
        var error = $(".jquery_panel_error");           //错误层
        var option = {
            url: $.fn.panel.defaults.script,
            // dataType: 'script',
            beforeSend: function(XMLHttpRequest) {
                btn.attr("disabled", "true").val("Sending..."); //发送前事件
            },
            complete: function(XMLHttpRequest, textStatus) {
                btn.attr("disabled", "").val("Submit"); //发送完成事件
            },
            data: { Message: message.val(), SecurityCode: codebox.val() }, //发送服务器数据
            success: function(data, textStatus) {//成功事件
                switch (data) {
                    case "UniqueCodeError":
                        error.show().empty().text("Security Code Error");
                        break;
                    case "Error":
                        error.show().empty().text("System Error");
                        break;
                    case "Succeed":
                        error.hide();
                        alert(data);
                        break;
                }
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {//发送失败事件
                error.show().empty().text(textStatus);
            }
        };
        //ajax 执行
        $.ajax(option);
    }

    //默认值
    $.fn.panel.defaults = {
        customerid: 0,
        left: 0,
        right: 0,
        bottom: 0,
        top: 0,
        title: 'Feedback',
        messagetip: '',
        messagebox: 'Click here to enter your message',
        messageboxerror: 'Your message should be between 20-1000 characters!',
        script: 'FastFeedBack.ashx',
        scurityuniquecodeurl: 'default.aspx?' + Math.random(),
        scurityuniquecodeerror: 'Scurity Code is required'
    };

})(jQuery);