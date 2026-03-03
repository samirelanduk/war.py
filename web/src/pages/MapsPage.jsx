import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

const MapsPage = () => {

  const [maps, setMaps] = useState(null);

  useEffect(() => {
    fetch("/api/maps/")
      .then(response => response.json())
      .then(data => setMaps(data));
  }, []);

  if (!maps) return <div>Loading...</div>;

  return (
    <div>
      <h1>Maps</h1>
      <Link to="/">Home</Link>

      <div className="flex flex-wrap mt-4">
        {maps.map(map => (
          <div key={map.id} className="w-1/4">
            <Link to={`/maps/${map.id}`}>
              <div>{map.name}</div>
              <div>{map.width}x{map.height}</div>
            </Link>
          </div>
        ))}
      </div>
    </div>
  );
};

MapsPage.propTypes = {
  
};

export default MapsPage;