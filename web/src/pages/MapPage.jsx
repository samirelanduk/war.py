import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";

const MapPage = () => {
  const { id } = useParams();
  const [map, setMap] = useState(null);

  useEffect(() => {
    fetch(`/api/maps/${id}/`)
      .then(response => response.json())
      .then(data => setMap(data));
  }, [id]);

  if (!map) return <div>Loading...</div>;

  const tileSize = 48;
  const mapWidth = map.width * tileSize;
  const mapHeight = map.height * tileSize;

  const colors = {
    G: "bg-green-500",
    S: "bg-blue-500",
    F: "bg-green-800",
    M: "bg-yellow-700",
    V: "bg-cyan-500",
    R: "bg-gray-400",
    B: "bg-gray-500",
  };

  const tileColor = (tile) => {
    return colors[tile.type] || "bg-black";
  };

  return (
    <div>
      <h1 className="text-2xl font-bold">{map.name}</h1>

      <div className="relative" style={{ width: mapWidth, height: mapHeight }}>
        {map.tiles.map(tile => (
          <div key={tile.id} className="absolute" style={{ left: tile.x * tileSize, top: tile.y * tileSize }}>
            <div className={`${tileColor(tile)}`} style={{ width: tileSize, height: tileSize }}></div>
          </div>
        ))}
      </div>

      <Link to="/maps">Back to maps</Link>
    </div>
  );
};

MapPage.propTypes = {
  
};

export default MapPage;