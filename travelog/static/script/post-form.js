$(document).on('change', '#id_post_image1', function(){
        if (!this.files.length) {
            console.log("false")
            return;
        }
        console.log("true")
        var file = $(this).prop('files')[0];
        var fr = new FileReader();
        $('#img_post1').css('background-image', 'none');
        fr.onload = function() {
            $('#img_post1').css('background-image', 'url(' + fr.result + ')');
        }
        fr.readAsDataURL(file);
        $("#img_post1 img").css('opacity', 0);
});

$(document).on('change', '#id_post_image2', function(){
    if (!this.files.length) {
        console.log("false")
        return;
    }
    console.log("true")
    var file = $(this).prop('files')[0];
    var fr = new FileReader();
    $('#img_post2').css('background-image', 'none');
    fr.onload = function() {
        $('#img_post2').css('background-image', 'url(' + fr.result + ')');
    }
    fr.readAsDataURL(file);
    $("#img_post2 img").css('opacity', 0);
});

$(document).on('change', '#id_post_image3', function(){
    if (!this.files.length) {
        console.log("false")
        return;
    }
    console.log("true")
    var file = $(this).prop('files')[0];
    var fr = new FileReader();
    $('#img_post3').css('background-image', 'none');
    fr.onload = function() {
        $('#img_post3').css('background-image', 'url(' + fr.result + ')');
    }
    fr.readAsDataURL(file);
    $("#img_post3 img").css('opacity', 0);
});

$(document).on('change', '#id_post_image4', function(){
    if (!this.files.length) {
        console.log("false")
        return;
    }
    console.log("true")
    var file = $(this).prop('files')[0];
    var fr = new FileReader();
    $('#img_post4').css('background-image', 'none');
    fr.onload = function() {
        $('#img_post4').css('background-image', 'url(' + fr.result + ')');
    }
    fr.readAsDataURL(file);
    $("#img_post4 img").css('opacity', 0);
});
