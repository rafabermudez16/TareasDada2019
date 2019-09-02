/ ** *
 * abs.js
 * *
 * te da el valor absoluto de un número
 * /

const  abs  =  function ( num ) {
    return num < 0  ? num * - 1  : num
}

consola . log ( abs ( 20 )) // 20
consola . log ( abs ( 0 )) // 0
consola . log ( abs ( - 31 )) // 31
