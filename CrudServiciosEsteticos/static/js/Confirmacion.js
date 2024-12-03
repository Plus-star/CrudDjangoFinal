(function(){
    
    const btnEliminacion =document.querySelectorAll(".btnEliminacion")

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) =>{
            const confirmar=confirm('¿Estas seguro?');
            if(!confirmar){
                e.preventDefault();
            }
        })
    })

})();