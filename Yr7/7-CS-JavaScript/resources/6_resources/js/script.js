window.onload = function(){
    var images = document.getElementById('badges1').getElementsByTagName('img');
    var JSCountBox = document.getElementById('textCount');
    var progress = images.length/12*100;
    JSCountBox.innerHTML = JSCountBox.innerHTML + 'Total Badges gained = ' + images.length;
    document.getElementById('progressBarFill').style.width = progress+'%';
}
