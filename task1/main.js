import './style.css';
import {Map, View, Feature} from 'ol';
import TileLayer from 'ol/layer/Tile';
import OSM from 'ol/source/OSM';
import { Polygon } from 'ol/geom';
import VectorLayer from 'ol/layer/Vector';
import VectorSource from 'ol/source/Vector';
import { fromLonLat } from 'ol/proj';

// map initialization
const map = new Map({
  target: 'map',
  layers: [
    new TileLayer({
      source: new OSM()
    })
  ],
  view: new View({
    center: [0, 0],
    zoom: 2
  })
});

// fetch the polygon coordinates from polygon.json
fetch('polygon.json')
  .then((response) => response.json())  // convert the responde to JSON
  .then((data) => {
      // transform the coodrinates to the map's projection
      const transformedCoordinates = data.polygon.map(coordinates => fromLonLat(coordinates));
      // create a polygon geometry
      const polygon = new Polygon([transformedCoordinates]);
      // create a feature with the polygon geometry
      const feature = new Feature({geometry: polygon});
      // create a vector layer to display the polygon
      const vectorLayer = new VectorLayer({
        source: new VectorSource({
          features: [feature]
        })
      });
      
      map.addLayer(vectorLayer);  // add the vector layer to the map
      map.getView().fit(feature.getGeometry().getExtent()); // center the map on the polygon and zoom in
    
      
  });