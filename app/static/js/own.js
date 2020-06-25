<script>
function updateProgress(element){
    var weight = element.attributes.weight;
    weight = weight + (100/19);

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

var doc = new jsPDF();
var specialElementHandlers = {
    '#editor': function (element, renderer) {
        return true;
    }
};

$('#btGerarPDF').click(function () {
    doc.fromHTML($('#conteudo').html(), 15, 15, {
        'width': 170,
            'elementHandlers': specialElementHandlers
    });
    doc.save('exemplo-pdf.pdf');
});

</script>
