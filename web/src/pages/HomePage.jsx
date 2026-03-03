import { Link } from "react-router-dom";

const HomePage = () => {
  return (
    <div>
      <h1>Home</h1>
      <Link to="/maps">Maps</Link>
    </div>
  );
};

HomePage.propTypes = {
  
};

export default HomePage;