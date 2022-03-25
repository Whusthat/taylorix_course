// Init on pageload
let before_loadtime = new Date().getTime();
window.onload = () => {
    let page_load_container = document.getElementById('page-load')
    let after_loadtime = new Date().getTime()
    let time_to_load_page = (after_loadtime - before_loadtime) / 1000
    page_load_container.innerHTML = 'Buildtime: '+ time_to_load_page + ' sek'
}