const Tile = props => {

  const { tile } = props;

  const tileSize = 48;

  const colors = {
    GR: "bg-green-400",
    SE: "bg-blue-500",
    FR: "bg-green-800",
    MT: "bg-yellow-700",
    RV: "bg-cyan-500",
    RO: "bg-gray-400",
    BR: "bg-gray-500",
    BE: "bg-yellow-600",
    RE: "bg-purple-500",

    CT: "bg-zinc-700",
    FC: "bg-zinc-800",
    PO: "bg-zinc-900",
    AP: "bg-zinc-950",
  };

  const playerColors = [
    "border-red-700",
    "border-blue-700",
    "border-green-500",
    "border-yellow-500",
  ]

  const tileColor = (tile) => {
    return colors[tile.type] || "bg-black";
  };

  const border = (tile) => {
    return tile.owner ? `border-4 ${playerColors[tile.owner - 1]}` : "";
  };

  return (
    <div
      className="absolute"
      style={{ left: (tile.x - 1) * tileSize, top: (tile.y - 1) * tileSize }}
    >
      <div className={`${tileColor(tile)} ${border(tile)}`} style={{ width: tileSize, height: tileSize }}></div>
    </div>
  );
};

Tile.propTypes = {
  
};

export default Tile;