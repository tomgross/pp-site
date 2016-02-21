$(document).ready(function(){
  $(window).resize(function(){
    if($(window).width() >= 768){
      $('.clickable-dropdown').on('click', function(){
        window.location.href=$(this).attr('href');
      });
    }
  }).resize();
});

$(window).scroll(function() {

    if ($(this).scrollTop()>0)
     {
        $('#top-row').fadeOut('fast', function() {
    $( "#header" ).height( 125 );
    $("#margin-top").css({'margin-top': 125});
  });
     }
    else
     {
      $('#top-row').fadeIn('slow');
     }
 });


