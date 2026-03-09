import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

const MapsPage = () => {

  const [maps, setMaps] = useState(null);
  const [selectedMap, setSelectedMap] = useState(null);

  useEffect(() => {
    fetch("/api/maps/")
      .then(response => response.json())
      .then(data => setMaps(data));
  }, []);

  if (!maps) return <div>Loading...</div>;

  return (
    <div>
      <h1 className="text-2xl font-bold">New Game</h1>
      <Link to="/" className="text-blue-500">Home</Link>

      <div className="mt-4">
        {maps.map(map => (
          <div
            className={`cursor-pointer p-2 border border-gray-300 w-96 rounded-md ${selectedMap?.id === map.id ? "bg-gray-100" : ""}`}
            onClick={() => setSelectedMap(map)}
          >
            <div>{map.name}</div>
            <div>{map.width}x{map.height}</div>
          </div>
        ))}
      </div>

      <button className={`mt-4 bg-blue-500 text-white px-4 py-2 rounded-md ${selectedMap ? "opacity-100" : "opacity-50 cursor-not-allowed"}`}>
        Start game
      </button>
    </div>
  );
};

MapsPage.propTypes = {
  
};

export default MapsPage;