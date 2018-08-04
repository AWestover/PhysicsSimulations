let chart = new Chartist.Line('.ct-chart', {series: [[0,1]]}, {showPoint:false});    
function updatePlot(x)
{
  chart.update({series: x}, {showPoint: false});
}
function randPoints(n)
{
  let o = [];
  let r = [];
  for (let i = 0; i < n; i++)
  {
    let tmp = Math.sin(0.2*i);
    o.push((Math.random()-0.5)*0.8 + tmp);
    r.push(tmp);
  }
  return [o];
}
function randUpdate()
{
  updatePlot(randPoints(100));
}
randUpdate();
setInterval(randUpdate, 2000);