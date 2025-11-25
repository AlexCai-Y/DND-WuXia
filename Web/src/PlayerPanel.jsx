import { io } from "socket.io-client";
// const socket = io("http://localhost:3001");

import { useState, useRef, useEffect } from "react";
import { motion } from "framer-motion";

// Sample targets
const targets = [
  { id: 1, name: "Goblin", hp: 30, mp: 30, initials: "G" },
  { id: 2, name: "Orc", hp: 50, mp: 30, initials: "O" },
  { id: 3, name: "Troll", hp: 80, mp: 30, initials: "T" },
];

// Battleground variables
const rows = 10;
const cols = 10;
const cellSize = 40;

const minWidth = cols * cellSize;
const minHeight = rows * cellSize;




const PlayerUI = () => {
  const [width, setWidth] = useState(minWidth);
  const [height, setHeight] = useState(minHeight);
  const [playerPosition, setPlayerPosition] = useState(0);
  const [constraints, setConstraints] = useState({
    top: -1000,
    bottom: -1000,
    left: 1000,
    right: 1000,
  });
  const containerRef = useRef(null);
  
 // Dynamically update drag constraint
  useEffect(() => {
    if (containerRef.current) {
      const { clientWidth, clientHeight } = containerRef.current;
      setConstraints({
        left: 0 - Math.max(0, (clientWidth) / 2),
        top: 0 - Math.max(0, (clientHeight) / 2),
        right: Math.max(0, (clientWidth - width) / 2),
        bottom: Math.max(0, (clientHeight - height) / 2),
      });
    }
  }, [width, height]);

  // Resize handler
  const handleWheel = (e) => {
    e.preventDefault();
    let newWidth = width + (e.deltaY < 0 ? 20 : -20);
    let newHeight = height + (e.deltaY < 0 ? 20 : -20);
    if (containerRef.current) {
      const { clientWidth, clientHeight } = containerRef.current;
      newWidth = Math.max(minWidth, newWidth);
      newHeight = Math.max(minHeight, newHeight);
    }
    setWidth(newWidth);
    setHeight(newHeight);
  };

  return (
    <div className="flex h-screen bg-gray-900 p-4 gap-4">
      {/* 先攻*/}
      <div className="bg-gray-800 rounded-2xl p-3 shadow-lg flex flex-col">
        <h2 className="text-xl mb-2 sticky top-0 bg-gray-800 z-10 text-white">
          角色
        </h2>
        <ul className="overflow-y-auto space-y-2 max-h-[calc(100vh-50px)]">
          {targets.map((target) => (
            <li
              key={target.id}
              className="flex items-center p-2 hover:bg-gray-700 rounded cursor-pointer transition-colors duration-200"
            >
              <div className="w-8 h-8 rounded-full bg-blue-500 flex-shrink-0 flex items-center justify-center text-white font-bold mr-2">
                {target.initials}
              </div>
              <div className="flex flex-col">
                <span className="font-semibold text-white">{target.name}</span>
              </div>
            </li>
          ))}
        </ul>
      </div>

      {/* 地圖 */}
      <div
        ref={containerRef}
        className="w-3/4 h-full flex justify-center items-center relative bg-gray-800 rounded-2xl p-4 overflow-hidden" // <-- overflow-hidden masks battleground
      >
        <motion.div
          drag
          dragConstraints={constraints}
          dragElastic={0}
          className="bg-black rounded-2xl shadow-lg p-2 relative"
          style={{ width: width, height: height }}
          onWheel={handleWheel}
        >
          {/* 10x10 Grid */}
          <div
            className="grid gap-[4px] w-full h-full"
            style={{
              gridTemplateColumns: `repeat(${cols}, 1fr)`,
              gridTemplateRows: `repeat(${rows}, 1fr)`,
            }}
          >
            {Array.from({ length: rows * cols }).map((_, i) => (
              <div
                key={i}
                className="border border-gray-700 w-full h-full relative flex items-center justify-center"
              >
                {playerPosition === i && (
                  <div className="absolute w-8 h-8 rounded-full bg-blue-500 flex items-center justify-center text-white font-bold">
                    P
                  </div>
                )}
              </div>
            ))}
          </div>
        </motion.div>
      </div>
    </div>
  );
};
export default PlayerUI;
