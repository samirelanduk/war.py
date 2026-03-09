import { Link } from "react-router-dom";

const HomePage = () => {
  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <h1 className="text-2xl font-bold">Home</h1>
      <Link to="/maps">Maps</Link>
      <Link to="/games/new">New Game</Link>
      <Link to="/games">Games</Link>
    </div>
  );
};

HomePage.propTypes = {
  
};

export default HomePage;