import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import MapsPage from "./pages/MapsPage";
import NewGamePage from "./pages/NewGamePage";
import MapPage from "./pages/MapPage";
import GamesPage from "./pages/GamesPage";

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/maps" element={<MapsPage />} />
        <Route path="/maps/:id" element={<MapPage />} />
        <Route path="/games" element={<GamesPage />} />
        <Route path="/games/new" element={<NewGamePage />} />
      </Routes>
    </BrowserRouter>
  );
};

App.propTypes = {
  
};

export default App;