!function(t,a){"function"==typeof define&&define.amd?define([],function(){return t.jCaptcha=a()}):"object"==typeof module&&module.exports?module.exports=a():t.jCaptcha=a()}(this,function(){"use strict";var t=function(t,a){return"function"!=typeof NodeList.prototype.forEach&&(NodeList.prototype.forEach=Array.prototype.forEach),Object.keys(a).forEach(function(e){t[e]=a[e]}),t},a=function(){c=Math.round(8*Math.random())+1,n=Math.round(8*Math.random())+1,i=c+n},e=function(t,a,e){!e&&t[0].insertAdjacentHTML("beforebegin",'<canvas class="jCaptchaText"></canvas>'),this.$captchaText=this.$captchaText||document.getElementsByClassName("jCaptchaText"),this.$jCaptchaTextContext=this.$jCaptchaTextContext||this.$captchaText[0].getContext("2d"),this.$captchaText[0].width=a.canvasWidth,this.$captchaText[0].height=a.canvasHeight,this.$jCaptchaTextContext.textBaseline="top",this.$jCaptchaTextContext.font=a.canvasFontSize+" "+a.canvasFontFamily,this.$jCaptchaTextContext.textAlign="left",this.$jCaptchaTextContext.fillStyle=a.canvasFillStyle,this.$jCaptchaTextContext.fillText(c+" + "+n+" "+a.requiredValue,0,0)},i=void 0,c=void 0,n=void 0,o=function(i){this.options=i?t(this.options,i):this.options,this.$captchaInput=document.getElementsByClassName(this.options.el),a(),e.apply(this,[this.$captchaInput,this.options])};return o.prototype={options:{el:"jCaptcha",requiredValue:"*",resetOnError:!0,focusOnError:!0,clearOnSubmit:!0,canvasWidth:50,canvasHeight:15,canvasFontSize:"1.5rem",canvasFontFamily:"Arial",canvasFillStyle:"#ddd",callback:null},validate:function(){this.callbackReceived=this.callbackReceived||"function"==typeof this.options.callback,this.$captchaInput[0].value!=i?(this.callbackReceived&&this.options.callback("error",this.$captchaInput),!0===this.options.resetOnError&&this.reset(),!0===this.options.focusOnError&&this.$captchaInput[0].focus(),!0===this.options.clearOnSubmit&&(this.$captchaInput[0].value="")):(this.callbackReceived&&this.options.callback("success",this.$captchaInput),!0===this.options.clearOnSubmit&&(this.$captchaInput[0].value=""))},reset:function(){a(),e.apply(this,[this.$captchaInput,this.options,!0])}},o});