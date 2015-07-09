var imageArray

window.onload = function()
{
    imageArray = document.getElementById('badges1').getElementsByTagName('img');
    var textCount = document.getElementById('textCount');
    textCount.innerHTML = imageArray.length;
};
