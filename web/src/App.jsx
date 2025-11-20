import { BrowserRouter, Routes, Route } from "react-router-dom";
import GMPanel from "./GMPanel";
import PlayerPanel from "./PlayerPanel";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/gm" element={<GMPanel />} />
        <Route path="/player" element={<PlayerPanel />} />
      </Routes>
    </BrowserRouter>
  );
}