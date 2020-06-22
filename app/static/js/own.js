<script>

function chamar1(id){
  var captar = document.getElementById(id).value;
  return Number(captar);

}

function chamar2(id,unit){
  var captar = document.getElementById(id).value;
  va captarunit = document.getElementById(unit).value;
  return ([Number(captar), unit]);

}

function change(id){
  captar = document.getElementById(id).style;
  percent = Number(captar.slice(7,9));
  x = 100/19;

  percent = percent + x;
  document.getElementById(id).style = percent;
  document.getElementById(id).innerHTML = "A barra de progresso está Funcionando"

}

function draw(bw, h, nbar, n, o, ot ){

  var canv = document.getElementById("myCanvas");
  var concrete = canv.getContext("2d");
  var rebar = canv.getContext("2d");
  var cord1 = c+(ot/2);
  var cord2 = bw-(c*2)-(ot);
  var cord3 = h-(c*2)-(ot);

  concrete.fillStyle = "#d3d9df";
  concrete.fillRect(0, 0, bw, h);

  concrete.lineWidth = ot;
  concrete.strokeRect(cord1, cord1, cord2 , cord3);

  rebar.strokeStyle = 'black';
  rebar.fillStyle = 'black';
  rebar.arc(bw/2,h/2,o/2,0,Math.PI*2);
  rebar.stroke();
  rebar.fill();

  x = draw(200,500,6,2,10,5, 25)

}

</script>
