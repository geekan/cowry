$("your_form_id").submit(function(e){
    $.ajax({
        url: 'your url',
        type: "PUT",
        data: $("your_form_id").serialize(),
        cache: false,
        dataType: "text",
        success: function(data){
            do_something()
        },
        error: function() {
            console.log("ERROR");
        }
    });
});
