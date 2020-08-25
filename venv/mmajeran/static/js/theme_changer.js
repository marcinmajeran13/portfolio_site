var spacegray = document.querySelector('#spacegray')
var purple = document.querySelector('#purple')
var green = document.querySelector('#green')
var brown = document.querySelector('#brown')

function change_background(color) {
    document.body.style.background = localStorage.getItem('theme_color')
    }

function remember_color(color) {
    localStorage.setItem('theme_color', color)
}
purple.addEventListener('click', function(){ remember_color('#4e1e66')})
purple.addEventListener('click', function(){ change_background('#4e1e66')})

spacegray.addEventListener('click', function(){ remember_color('#352f38')})
spacegray.addEventListener('click', function(){ change_background('#352f38')})

green.addEventListener('click', function(){ remember_color('#0f421f')})
green.addEventListener('click', function(){ change_background('#0f421f')})

brown.addEventListener('click', function(){ remember_color('#361d09')})
brown.addEventListener('click', function(){ change_background('#361d09')})

//spacegray.addEventListener('click', function(){
//     document.body.style.background = '#352f38'
//})
//
//green.addEventListener('click', function(){
//     document.body.style.background = '#0f421f'
//})
//
//brown.addEventListener('click', function(){
//     document.body.style.background = '#361d09'
//})

