function toggleTopic(button){const panel=document.getElementById(button.getAttribute('aria-controls'));const open=button.getAttribute('aria-expanded')==='true';panel.hidden=open;button.setAttribute('aria-expanded',String(!open))}
function openModal(src){const modal=document.getElementById('module-modal');document.getElementById('module-frame').src=src;modal.showModal()}
function closeModal(){document.getElementById('module-modal').close()}
document.addEventListener('DOMContentLoaded',()=>{document.querySelectorAll('.accordion').forEach(b=>{document.getElementById(b.getAttribute('aria-controls')).hidden=true;b.setAttribute('aria-expanded','false')});const modal=document.getElementById('module-modal');modal.addEventListener('click',e=>{if(e.target===modal)modal.close()})});
