$(document).ready(function(){
	var timer0 = null;
    var week = new Array( "日", "一", "二", "三", "四", "五", "六" );
    timer0 = setTimeout(showTime,10);
    function showTime() {
               clearTimeout(timer0);
               dt = new Date();
               var weekday = week[dt.getDay()];
               var tp = document.getElementById("timePlace");
               result = dt.toLocaleDateString()+" 星期"+weekday+" "+dt.toLocaleTimeString();
               tp.innerHTML = result;
               timer0 = setTimeout(showTime,1000);
            }
			});

$(document).ready(function(){
     $('#datetimepickerA').datetimepicker({
        format: 'YYYY-MM-DD',
        locale: moment.locale('zh-cn'),
      })
	   });

$(document).ready(function(){
     $('#datetimepicker0').datetimepicker({
        format: 'YYYY-MM-DD hh:mm ',
        locale: moment.locale('zh-cn'),
      })
	   });
$(document).ready(function(){
     $('#datetimepicker1').datetimepicker({
        format: 'YYYY-MM-DD hh:mm ',
        locale: moment.locale('zh-cn'),
      })
	   });
$(document).ready(function(){
     $('#datetimepicker2').datetimepicker({
        format: 'YYYY-MM-DD hh:mm ',
        locale: moment.locale('zh-cn'),
      })
	   });
$(document).ready(function(){
     $('#datetimepicker3').datetimepicker({
        format: 'YYYY-MM-DD hh:mm ',
        locale: moment.locale('zh-cn'),
      })
	   });
$(document).ready(function(){
     $('#datetimepicker4').datetimepicker({
        format: 'YYYY-MM-DD hh:mm ',
        locale: moment.locale('zh-cn'),
      })
	   });
$(document).ready(function(){
     $('#datetimepicker5').datetimepicker({
        format: 'YYYY-MM-DD hh:mm ',
        locale: moment.locale('zh-cn'),
      })
	   });
$(document).ready(function(){
     $('#datetimepicker6').datetimepicker({
        format: 'YYYY-MM-DD hh:mm ',
        locale: moment.locale('zh-cn'),
      })
	   });
$(document).ready(function(){
     $('#datetimepicker7').datetimepicker({
        format: 'YYYY-MM-DD hh:mm ',
        locale: moment.locale('zh-cn'),
      })
	   });
$(document).ready(function(){
     $('#datetimepicker8').datetimepicker({
        format: 'YYYY-MM-DD hh:mm ',
        locale: moment.locale('zh-cn'),
      })
	   });
$(document).ready(function(){
     $('#datetimepicker9').datetimepicker({
        format: 'YYYY-MM-DD hh:mm ',
        locale: moment.locale('zh-cn'),
      })
	   });
$(document).ready(function(){
     $('#datetimepicker10').datetimepicker({
        format: 'YYYY-MM-DD hh:mm ',
        locale: moment.locale('zh-cn'),
      })
	   });
$(document).ready(function(){
     $('#datetimepicker11').datetimepicker({
        format: 'YYYY-MM-DD hh:mm ',
        locale: moment.locale('zh-cn'),
      })
	   });
$(document).ready(function(){
     $('#datetimepicker12').datetimepicker({
        format: 'YYYY-MM-DD hh:mm ',
        locale: moment.locale('zh-cn'),
      })
	   });
$(document).ready(function(){
     $('#datetimepicker13').datetimepicker({
        format: 'YYYY-MM-DD hh:mm ',
        locale: moment.locale('zh-cn'),
      })
	   });
$(document).ready(function(){
     $('#datetimepicker14').datetimepicker({
        format: 'YYYY-MM-DD hh:mm ',
        locale: moment.locale('zh-cn'),
      })
	   });
$(document).ready(function(){
     $('#datetimepicker15').datetimepicker({
        format: 'YYYY-MM-DD hh:mm ',
        locale: moment.locale('zh-cn'),
      })
	   });

$(function () {
    $("#ic-menu").click(function () {
        $(this).addClass('active');
        $("#msb-csb-xzy-menu").removeClass('active');
        $("#ic").show();
        $("#msb-csb-xzy").hide();
    })
})

$(function () {
    $("#msb-csb-xzy-menu").click(function () {
        $(this).addClass('active');
        $("#ic-menu").removeClass('active');
        $("#msb-csb-xzy").show();
        $("#ic").hide();
    })
})

//IC数据按钮切换
$(function () {
    $("#menu0").click(function () {
        $(this).addClass('active');
        $("#menu1").removeClass('active');
        $("#menu2").removeClass('active');
        $("#menu3").removeClass('active');
        $("#menu4").removeClass('active');
        $("#menu5").removeClass('active');
        $("#menu0-con").show();
        $("#menu1-con").hide();
        $("#menu2-con").hide();
        $("#menu3-con").hide();
        $("#menu4-con").hide();
        $("#menu5-con").hide();
    })
})

$(function () {
    $("#menu1").click(function () {
        $(this).addClass('active');
        $("#menu0").removeClass('active');
        $("#menu2").removeClass('active');
        $("#menu3").removeClass('active');
        $("#menu4").removeClass('active');
        $("#menu5").removeClass('active');
        $("#menu1-con").show();
        $("#menu0-con").hide();
        $("#menu2-con").hide();
        $("#menu3-con").hide();
        $("#menu4-con").hide();
        $("#menu5-con").hide();
    })
})

$(function () {
    $("#menu2").click(function () {
        $(this).addClass('active');
        $("#menu1").removeClass('active');
        $("#menu0").removeClass('active');
        $("#menu3").removeClass('active');
        $("#menu4").removeClass('active');
        $("#menu5").removeClass('active');
        $("#menu2-con").show();
        $("#menu1-con").hide();
        $("#menu0-con").hide();
        $("#menu3-con").hide();
        $("#menu4-con").hide();
        $("#menu5-con").hide();
    })
})

$(function () {
    $("#menu3").click(function () {
        $(this).addClass('active');
        $("#menu1").removeClass('active');
        $("#menu2").removeClass('active');
        $("#menu0").removeClass('active');
        $("#menu4").removeClass('active');
        $("#menu5").removeClass('active');
        $("#menu3-con").show();
        $("#menu1-con").hide();
        $("#menu2-con").hide();
        $("#menu0-con").hide();
        $("#menu4-con").hide();
        $("#menu5-con").hide();
    })
})

$(function () {
    $("#menu4").click(function () {
        $(this).addClass('active');
        $("#menu1").removeClass('active');
        $("#menu2").removeClass('active');
        $("#menu3").removeClass('active');
        $("#menu0").removeClass('active');
        $("#menu5").removeClass('active');
        $("#menu4-con").show();
        $("#menu1-con").hide();
        $("#menu2-con").hide();
        $("#menu3-con").hide();
        $("#menu0-con").hide();
        $("#menu5-con").hide();
    })
})

$(function () {
    $("#menu5").click(function () {
        $(this).addClass('active');
        $("#menu1").removeClass('active');
        $("#menu2").removeClass('active');
        $("#menu3").removeClass('active');
        $("#menu4").removeClass('active');
        $("#menu0").removeClass('active');
        $("#menu5-con").show();
        $("#menu1-con").hide();
        $("#menu2-con").hide();
        $("#menu3-con").hide();
        $("#menu4-con").hide();
        $("#menu0-con").hide();
    })
})

//
$(function () {
    $("#menu0-c").click(function () {
        $(this).addClass('active');
        $("#menu1-c").removeClass('active');
        $("#menu2-c").removeClass('active');
        $("#menu3-c").removeClass('active');
        $("#menu4-c").removeClass('active');
        $("#menu5-c").removeClass('active');
        $("#menu0-con-c").show();
        $("#menu1-con-c").hide();
        $("#menu2-con-c").hide();
        $("#menu3-con-c").hide();
        $("#menu4-con-c").hide();
        $("#menu5-con-c").hide();
    })
})

$(function () {
    $("#menu1-c").click(function () {
        $(this).addClass('active');
        $("#menu0-c").removeClass('active');
        $("#menu2-c").removeClass('active');
        $("#menu3-c").removeClass('active');
        $("#menu4-c").removeClass('active');
        $("#menu5-c").removeClass('active');
        $("#menu1-con-c").show();
        $("#menu0-con-c").hide();
        $("#menu2-con-c").hide();
        $("#menu3-con-c").hide();
        $("#menu4-con-c").hide();
        $("#menu5-con-c").hide();
    })
})

$(function () {
    $("#menu2-c").click(function () {
        $(this).addClass('active');
        $("#menu1-c").removeClass('active');
        $("#menu0-c").removeClass('active');
        $("#menu3-c").removeClass('active');
        $("#menu4-c").removeClass('active');
        $("#menu5-c").removeClass('active');
        $("#menu2-con-c").show();
        $("#menu1-con-c").hide();
        $("#menu0-con-c").hide();
        $("#menu3-con-c").hide();
        $("#menu4-con-c").hide();
        $("#menu5-con-c").hide();
    })
})

$(function () {
    $("#menu3-c").click(function () {
        $(this).addClass('active');
        $("#menu1-c").removeClass('active');
        $("#menu2-c").removeClass('active');
        $("#menu0-c").removeClass('active');
        $("#menu4-c").removeClass('active');
        $("#menu5-c").removeClass('active');
        $("#menu3-con-c").show();
        $("#menu1-con-c").hide();
        $("#menu2-con-c").hide();
        $("#menu0-con-c").hide();
        $("#menu4-con-c").hide();
        $("#menu5-con-c").hide();
    })
})

$(function () {
    $("#menu4-c").click(function () {
        $(this).addClass('active');
        $("#menu1-c").removeClass('active');
        $("#menu2-c").removeClass('active');
        $("#menu3-c").removeClass('active');
        $("#menu0-c").removeClass('active');
        $("#menu5-c").removeClass('active');
        $("#menu4-con-c").show();
        $("#menu1-con-c").hide();
        $("#menu2-con-c").hide();
        $("#menu3-con-c").hide();
        $("#menu0-con-c").hide();
        $("#menu5-con-c").hide();
    })
})

$(function () {
    $("#menu5-c").click(function () {
        $(this).addClass('active');
        $("#menu1-c").removeClass('active');
        $("#menu2-c").removeClass('active');
        $("#menu3-c").removeClass('active');
        $("#menu4-c").removeClass('active');
        $("#menu0-c").removeClass('active');
        $("#menu5-con-c").show();
        $("#menu1-con-c").hide();
        $("#menu2-con-c").hide();
        $("#menu3-con-c").hide();
        $("#menu4-con-c").hide();
        $("#menu0-con-c").hide();
    })
})

