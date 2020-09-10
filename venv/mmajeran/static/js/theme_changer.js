var spacegray = document.querySelector('#spacegray')
var purple = document.querySelector('#purple')
var green = document.querySelector('#green')
var brown = document.querySelector('#brown')
var nav = document.querySelector('.navbar-custom')

function change_background(color) {
    document.body.style.background = localStorage.getItem('theme_color')
    nav.style.backgroundColor = localStorage.getItem('nav_color')
    }

function remember_color(color, navcol) {
    localStorage.setItem('theme_color', color)
    localStorage.setItem('nav_color', navcol)
}

document.querySelector('.top-page').addEventListener('mouseover', function(){
    document.querySelector('.title-icon').style.color = '#fdfd96'
})

document.querySelector('.top-page').addEventListener('mouseout', function(){
    document.querySelector('.title-icon').style.color = 'gray'
})

function adds() {


    purple.addEventListener('click', function(){ remember_color('#370752','#5f1c85')})
    purple.addEventListener('click', function(){ change_background('#370752')})

    spacegray.addEventListener('click', function(){ remember_color('#242625','#303030')})
    spacegray.addEventListener('click', function(){ change_background('#242625')})

    green.addEventListener('click', function(){ remember_color('#0f421f','#415e50')})
    green.addEventListener('click', function(){ change_background('#0f421f')})

    brown.addEventListener('click', function(){ remember_color('#614805','#997208')})
    brown.addEventListener('click', function(){ change_background('#614805')})
 }


