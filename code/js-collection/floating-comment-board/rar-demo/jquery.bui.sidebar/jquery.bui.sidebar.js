/* NAME:	jquery.bui.sidebar.js
 * VERSION:	0.0.1
 * DATE：	2013-4-11
 * AUTHOR：	blacklaw
 * HOME:	http://townke.com
 * EMAIL:	2577927146@qq.com
 * DEPENDS:
 *		jquery-1.9.1.js
 *		jquery.bui.sidebar.css
 */

(function($,undefined){
	//alert('b');
	$.widget('bui.sidebar',{
		options:{
			top:null,
			width:200,
			background:null,
			handlerWidth:20,
			height:100,
			title:'扩展',
			titleE:'收缩',
			extend:false,
			handlerCSS:{
				right:0,
			},
			panelCSS:{
				opacity:0,
				width:0,
			},
			handlerECSS:{
				right:300,
			},
			panelECSS:{
				opacity:.7,
				width:300,
			}
		},
		_create:function(){

			if(!$.bui.sidebar.elements){
				  $.bui.sidebar.elements=[];
				  $.bui.sidebar.handlers=[];
			}
			$.bui.sidebar.elements.push(this.element);
			var that=this;
			this.options.handlerECSS.right=this.options.panelECSS.width=this.options.width;
			this.element.handler=$('<div>').width(this.options.handlerWidth)
				.text(this.options.title)
				.height(this.options.height)
				.addClass('bui-sidebar-handler')
				.click(function(){
					that._toggle();
				});
			$.bui.sidebar.handlers.push(this.element.handler);
			this.element.width(0)
						.height('100%')
						.addClass('bui-sidebar');
			if(this.options.background){
				this.element.css('background',this.options.background);	
				this.element.handler.css('background',this.options.background);	
			}
			this.element.before(this.element.handler);
			this._repos(this.element.handler);
			$(window).resize(function(){that._repos(that.element.handler);});
		},
		_repos:function(obj){
			if(!this.options.top)
				this._center(obj);
			else
			 	obj.css('top',this.options.top);
		},
		_toggle:function(){
			

			if(!this.options.extend){
				this._collapseOthers();
				this.element.handler.text(this.options.title);
				this.element.handler.stop().animate(this.options.handlerECSS,200);
				this.element.stop().animate(this.options.panelECSS,200);
			} else {
				this.element.handler.text(this.options.title);
				this.element.handler.stop().animate(this.options.handlerCSS);
				this.element.stop().animate(this.options.panelCSS);
			}
			this.options.extend=!this.options.extend;
		},
		_collapseOthers:function(){
			//alert('c');
			for(i in $.bui.sidebar.elements){
				if($.bui.sidebar.elements[i].sidebar('option','extend')){
					$.bui.sidebar.elements[i].handler.trigger("click");
				}
			}
		},
		_center:function(obj){
			obj.css('top',function(){
				return ($(window).height()-$(this).height())/2;
			});
		}
	});
	
})(jQuery)