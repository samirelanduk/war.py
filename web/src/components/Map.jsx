import Tile from "./Tile";

const Map = props => {

  const { map } = props;

  return (
    <div className="relative">
      {map.tiles.map(tile => (
        <Tile key={tile.id} tile={tile} />
      ))}
    </div>
  );
};

Map.propTypes = {
  
};

export default Map;