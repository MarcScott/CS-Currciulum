var imageArray, progress

window.onload = function()
{
    imageArray = document.getElementById('badges1').getElementsByTagName('img');
    var textCount = document.getElementById('textCount');
    textCount.innerHTML = 'Total Badges gained = ' + imageArray.length;
    progress = imageArray.length/6*100;
    document.getElementById('progressBarFill').style.width = progress + '%';
};
