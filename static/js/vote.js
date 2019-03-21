
$(document).ready(function($) {


  $(document).on( "click", '#likes', function(){
            var walkerid;
            walkerid = $(this).attr("data-walkerid");
             $.get('/golden_leash/like_walker/', {walker_id: walkerid}, function(data){
                       $('#like_count').html(data);
                       $('#likes').hide();
                   });


  })();
  // unused dislike button
  // $(document).on( "click", '#dislikes', function(){
  //           var walkerid;
  //           walkerid = $(this).attr("data-walkerid");
  //            $.get('/golden_leash/dislike_walker/', {walker_id: walkerid}, function(data){
  //                      $('#like_count').html(data);
  //                      $('#dislikes').hide();
  //                  });
  // })();



})(jQuery);
