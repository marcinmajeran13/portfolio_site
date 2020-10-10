var spacegray = document.querySelector('#spacegray')
var purple = document.querySelector('#purple')
var green = document.querySelector('#green')
var mustard = document.querySelector('#mustard')
var nav = document.querySelector('.navbar-custom')
var title = document.querySelector('h1 a')
var title2 = document.querySelectorAll('.page-wrapper h1')
var post_title = document.querySelectorAll('.repair-title a')
var app_name = document.querySelectorAll('.app-name')
var btn = document.querySelector('.mybtn')
var i

function change_background() {
    document.body.style.background = localStorage.getItem('theme_color')
    nav.style.backgroundColor = localStorage.getItem('nav_color')
    title.style.color = localStorage.getItem('title_col')

    for (i=0; i < title2.length; i++) {
        title2[i].style.color = localStorage.getItem('title_col')
    }
    
    for (i=0; i < post_title.length; i++) {
        post_title[i].style.color = localStorage.getItem('title_col')
    }

    for (i=0; i < app_name.length; i++) {
        app_name[i].style.color = localStorage.getItem('title_col')
    }

     btn.style.backgroundColor = localStorage.getItem('title_col')
    }

function remember_color(color, navcol, title_col) {
    localStorage.setItem('theme_color', color)
    localStorage.setItem('nav_color', navcol)
    localStorage.setItem('title_col', title_col)
}

document.querySelector('.top-page').addEventListener('mouseover', function(){
    document.querySelector('.title-icon').style.color = '#fdfd96'
})

document.querySelector('.top-page').addEventListener('mouseout', function(){
    document.querySelector('.title-icon').style.color = 'gray'
})

document.querySelector('.top-page').addEventListener('touchstart', function(){
    document.querySelector('.title-icon').style.color = '#fdfd96'
})

document.querySelector('.top-page').addEventListener('touchend', function(){
    document.querySelector('.title-icon').style.color = 'gray'
})

function adds() {


    purple.addEventListener('click', function(){ remember_color('#370752','#5f1c85','#8140b3')})
    purple.addEventListener('click', function(){ change_background()})

    spacegray.addEventListener('click', function(){ remember_color('#242625','#303030','#8140b3')})
    spacegray.addEventListener('click', function(){ change_background()})

    green.addEventListener('click', function(){ remember_color('#0f421f','#415e50','#71ad90')})
    green.addEventListener('click', function(){ change_background()})

    mustard.addEventListener('click', function(){ remember_color('#614805','#ad9c6c','#d1bc82')})
    mustard.addEventListener('click', function(){ change_background()})
 }


