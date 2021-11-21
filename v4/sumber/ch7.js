

am5.ready(function() {

  var root = am5.Root.new("ch7");
  var value = 0;
  var data = generateChartData();
  root.setThemes([am5themes_Animated.new(root)]);
  var easing = am5.ease.linear;

  function generateChartData() {
            var chartData = [];
            var firstDate = new Date();
            firstDate.setDate(firstDate.getDate() - 1000);
            firstDate.setHours(0, 0, 0, 0);
          
            for (var i = 0; i < 100; i++) {
              var newDate = new Date(firstDate);
              newDate.setSeconds(newDate.getSeconds() + i);
              value += (Math.random() < 0.5 ? 1 : -1) * Math.random() * 10;        
              chartData.push({
              date: newDate.getTime(),
              value: value
              });
              }
    return chartData;
    }


  var chart = root.container.children.push(am5xy.XYChart.new(root, {
    focusable: true,
    panX: false,
    panY: false,
    wheelX: "panX",
    wheelY: "zoomX"
  }));
  
  var xAxis = chart.xAxes.push(am5xy.DateAxis.new(root, {
    minBulletDistance: 100,
    maxDeviation: 0.2,
    groupData: true,
    extraMax:0.1, 
    extraMin:-0.3,  
    baseInterval: {
      timeUnit: "second",
      count: 1
    },
    renderer: am5xy.AxisRendererX.new(root, {
      minGridDistance: 1000
    }),
    tooltip: am5.Tooltip.new(root, {})
  }));
  
  var yAxis = chart.yAxes.push(am5xy.ValueAxis.new(root, {
    renderer: am5xy.AxisRendererY.new(root, {})
  }));
  
  var series = chart.series.push(am5xy.LineSeries.new(root, {
    name: "Series 1",
    xAxis: xAxis,
    yAxis: yAxis,
    valueYField: "value",
    valueXField: "date",
   
    tooltip: am5.Tooltip.new(root, {
      pointerOrientation: "horizontal",
      labelText: "{valueY}"
    })
  }));
  var cursor = chart.set("cursor", am5xy.XYCursor.new(root, {
    xAxis: xAxis,
    behavior: "none"
  }));

  data[data.length - 1].bullet = true;
  series.data.setAll(data);
  series.fills.template.setAll({
    fillOpacity: 0.1,
    visible: true
  });
  series.strokes.template.setAll({
    strokeWidth: 1
  });
  
  series.bullets.push(function(root, series, dataItem) {  
    if (dataItem.dataContext.bullet) {    
      var container = am5.Container.new(root, {});
      var circle0 = container.children.push(am5.Circle.new(root, {
        radius: 5,
        fill: am5.color(0xff0000),
        
      }));
      var circle1 = container.children.push(am5.Circle.new(root, {
        radius: 5,
        fill: am5.color(0xff0000)
      }));
  
      circle1.animate({
        key: "radius",
        to: 20,
        duration: 100,
        easing: am5.ease.out(am5.ease.cubic),
        loops: Infinity
      });
      circle1.animate({
        key: "opacity",
        to: 0,
        from: 10,
        duration: 100,
        easing: am5.ease.out(am5.ease.cubic),
        loops: Infinity
      });
  
      return am5.Bullet.new(root, {
        locationX:undefined,
        sprite: container
      })
    }
  })
  
  
  
 function addData() {
  
  source.onmessage = function out(event) {
  var data = JSON.parse(event.data);
  var lastDataItem = series.dataItems[series.dataItems.length - 1];
  var lastValue = lastDataItem.get("valueY");
  
  var newValue = (data.v7);
  
  var lastDate = new Date(lastDataItem.get("valueX"));
  var time = am5.time.add(new Date(lastDate), "second", 1).getTime();
  series.data.removeIndex(0);
    

  series.data.push({
    date: time,
    value: newValue
  })

  var newDataItem = series.dataItems[series.dataItems.length - 1];
  newDataItem.animate({
    key: "valueYWorking",
    to: newValue,
    from: lastValue,
    duration: 200,
    easing: easing
  });

  newDataItem.bullets = [];
  newDataItem.bullets[0] = lastDataItem.bullets[0];
  newDataItem.bullets[0].get("sprite").dataItem = newDataItem;
  // reset bullets
  lastDataItem.dataContext.bullet = false;
  lastDataItem.bullets = [];


  var animation = newDataItem.animate({
    key: "locationX",
    to: 0.5,
    from: -0.5,
    duration: 100
  });
  if (animation) {
    var tooltip = xAxis.get("tooltip");
    if (tooltip && !tooltip.isHidden()) {
      animation.events.on("stopped", function () {
        xAxis.updateTooltip();
      })
    }
  }

}
}


setInterval(function () {
  addData() ;
}, 100)

chart.appear(1000, 100);
  
  });