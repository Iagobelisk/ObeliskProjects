function finalizar(){
    var res = document.getElementById('res')
    var res1 = document.getElementById('res1')
    var res2 = document.getElementById('res2')
    var res3 = document.getElementById('res3')
    var res4 = document.getElementById('res4')
    var res5 = document.getElementById('res5')
    var totImp = 0 
    var totMerc = 0
    var totGeral = 0
    var tot = 0
    var preco = 4.5
    var ICMS = 0.18
    var IPI = 0.04
    var PIS = 0.0186
    var COFINS = 0.0854
    var bon = 0.3
    if (qnt.value.length == 0 || emp.value.length == 0){
        window.alert('Digite os valores antes de prosseguir!')
    } else {
        Number.parseInt(qnt.value)
        res.innerHTML = `${emp.value} comprou a quantia de ${qnt.value} energéticos Accelerator.`
        res1.innerHTML = `Valor da compra SEM impostos foi de R$ ${(tot = preco * qnt.value).toFixed(2)}`
        res2.innerHTML = `O valor do ICMS foi de R$ ${(tot * ICMS).toFixed(2)}`
        res3.innerHTML = `O valor do IPI foi de R$ ${(tot * IPI).toFixed(2)}`
        res4.innerHTML = `O valor do PIS foi de R$ ${(tot * PIS).toFixed(2)}`
        res5.innerHTML = `O valor do COFINS foi de R$ ${(tot * COFINS).toFixed(2)}`

        totimp.innerHTML = `Total de impostos foi de R$ ${(tot * ICMS + tot * IPI + tot * PIS + tot * COFINS).toFixed(2)}`
        totmerc.innerHTML = `Valor da mercadoria R$ ${(preco * qnt.value).toFixed(2)}`
        totgeral.innerHTML = `O valor geral foi de R$ ${(preco * qnt.value + tot * ICMS + tot * IPI + tot * PIS + tot * COFINS).toFixed(2)}`

        
        
        
        
        
      
    }   
} 

    


