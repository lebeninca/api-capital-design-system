/* Tema ECharts da API Capital. GERADO por tokens/gerar_tokens.py a partir de DESIGN.md.
   Nao edite este arquivo: edite o DESIGN.md e rode o gerador.
   Uso: carregue echarts, depois este arquivo, depois echarts.init(el, 'api-capital'). */
(function(){
  var tema = {
    "color": [
      "#0D2A54",
      "#AA7D41",
      "#418ECE",
      "#171717",
      "#E4CB8D"
    ],
    "backgroundColor": "transparent",
    "textStyle": {
      "color": "#171717",
      "fontFamily": "Inter, system-ui, sans-serif",
      "fontSize": 15
    },
    "title": {
      "textStyle": {
        "color": "#171717",
        "fontFamily": "Inter, system-ui, sans-serif",
        "fontSize": 20,
        "fontWeight": 600
      },
      "subtextStyle": {
        "color": "rgba(23,23,23,0.5)",
        "fontFamily": "Inter, system-ui, sans-serif",
        "fontSize": 15,
        "fontWeight": 400
      }
    },
    "legend": {
      "textStyle": {
        "color": "#171717",
        "fontFamily": "Inter, system-ui, sans-serif",
        "fontSize": 14
      },
      "icon": "rect",
      "itemWidth": 14,
      "itemHeight": 14
    },
    "tooltip": {
      "backgroundColor": "#FFFFFF",
      "borderColor": "#E6E7E8",
      "borderWidth": 1,
      "textStyle": {
        "color": "#171717",
        "fontFamily": "Inter, system-ui, sans-serif",
        "fontSize": 15
      },
      "axisPointer": {
        "lineStyle": {
          "color": "rgba(23,23,23,0.5)",
          "width": 1
        },
        "crossStyle": {
          "color": "rgba(23,23,23,0.5)",
          "width": 1
        }
      }
    },
    "categoryAxis": {
      "axisLine": {
        "show": true,
        "lineStyle": {
          "color": "#E6E7E8",
          "width": 1
        }
      },
      "axisTick": {
        "show": false
      },
      "axisLabel": {
        "color": "rgba(23,23,23,0.5)",
        "fontFamily": "Inter, system-ui, sans-serif",
        "fontSize": 14
      },
      "splitLine": {
        "show": false
      },
      "splitArea": {
        "show": false
      }
    },
    "valueAxis": {
      "axisLine": {
        "show": false
      },
      "axisTick": {
        "show": false
      },
      "axisLabel": {
        "color": "rgba(23,23,23,0.5)",
        "fontFamily": "Inter, system-ui, sans-serif",
        "fontSize": 14
      },
      "splitLine": {
        "show": true,
        "lineStyle": {
          "color": "#E6E7E8",
          "width": 1
        }
      },
      "splitArea": {
        "show": false
      },
      "scale": false
    },
    "logAxis": {
      "axisLine": {
        "show": true,
        "lineStyle": {
          "color": "#E6E7E8",
          "width": 1
        }
      },
      "axisTick": {
        "show": false
      },
      "axisLabel": {
        "color": "rgba(23,23,23,0.5)",
        "fontFamily": "Inter, system-ui, sans-serif",
        "fontSize": 14
      },
      "splitLine": {
        "show": true,
        "lineStyle": {
          "color": "#E6E7E8",
          "width": 1
        }
      },
      "splitArea": {
        "show": false
      }
    },
    "timeAxis": {
      "axisLine": {
        "show": true,
        "lineStyle": {
          "color": "#E6E7E8",
          "width": 1
        }
      },
      "axisTick": {
        "show": false
      },
      "axisLabel": {
        "color": "rgba(23,23,23,0.5)",
        "fontFamily": "Inter, system-ui, sans-serif",
        "fontSize": 14
      },
      "splitLine": {
        "show": false
      },
      "splitArea": {
        "show": false
      }
    },
    "line": {
      "lineStyle": {
        "width": 2
      },
      "symbol": "circle",
      "symbolSize": 6,
      "smooth": false,
      "showSymbol": false
    },
    "bar": {
      "barMaxWidth": 56,
      "itemStyle": {
        "borderRadius": 0
      }
    },
    "pie": {
      "itemStyle": {
        "borderColor": "#FFFFFF",
        "borderWidth": 2
      },
      "label": {
        "color": "#171717",
        "fontFamily": "Inter, system-ui, sans-serif",
        "fontSize": 14
      }
    },
    "candlestick": {
      "itemStyle": {
        "color": "#0E7A47",
        "color0": "#B71313",
        "borderColor": "#0E7A47",
        "borderColor0": "#B71313"
      }
    },
    "scatter": {
      "symbolSize": 8
    },
    "graph": {
      "lineStyle": {
        "color": "#E6E7E8"
      }
    },
    "markLine": {
      "lineStyle": {
        "color": "rgba(23,23,23,0.5)",
        "type": "dashed",
        "width": 1
      },
      "label": {
        "color": "#171717",
        "fontFamily": "Inter, system-ui, sans-serif",
        "fontSize": 14
      }
    },
    "markPoint": {
      "itemStyle": {
        "color": "#AA7D41"
      },
      "label": {
        "color": "#FFFFFF"
      }
    },
    "visualMap": {
      "color": [
        "#0D2A54",
        "#418ECE",
        "#F4F4F4"
      ]
    },
    "dataZoom": {
      "borderColor": "#E6E7E8",
      "fillerColor": "rgba(13,42,84,0.08)",
      "handleStyle": {
        "color": "#0D2A54"
      }
    }
  };
  if (typeof echarts !== 'undefined') echarts.registerTheme('api-capital', tema);
  if (typeof window !== 'undefined') window.API_CAPITAL_TEMA_ECHARTS = tema;
})();
