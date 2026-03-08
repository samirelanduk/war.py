import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import Map from "../components/Map";

const MapPage = () => {
  const { id } = useParams();
  const [map, setMap] = useState(null);

  useEffect(() => {
    fetch(`/api/maps/${id}/`)
      .then(response => response.json())
      .then(data => setMap(data));
  }, [id]);

  if (!map) return <div>Loading...</div>;

  return (
    <div>
      <h1 className="text-2xl font-bold">{map.name}</h1>

      <Map map={map} />

      <Link to="/maps">Back to maps</Link>
    </div>
  );
};

MapPage.propTypes = {
  
};

export default MapPage;