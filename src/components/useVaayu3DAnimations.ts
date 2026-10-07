import { useEffect } from 'react';
import { Platform } from 'react-native';

const GLOBAL_STYLE_ID = 'vaayu-3d-animations-v10';

const CSS = `
@keyframes float3D {
  0%, 100% { transform: perspective(1000px) rotateY(6deg) rotateX(3deg) translateY(0px); }
  50% { transform: perspective(1000px) rotateY(-4deg) rotateX(6deg) translateY(-8px); }
}

@keyframes float3DReverse {
  0%, 100% { transform: perspective(1000px) rotateY(-6deg) rotateX(3deg) translateY(0px); }
  50% { transform: perspective(1000px) rotateY(4deg) rotateX(6deg) translateY(-8px); }
}

@keyframes flamePulse {
  0%, 100% { transform: scale(1) rotate(0deg); filter: drop-shadow(0 0 15px rgba(0,229,255,0.6)); }
  50% { transform: scale(1.05) rotate(2deg); filter: drop-shadow(0 0 25px rgba(0,229,255,1)); }
}

@keyframes waveMeniscus {
  0%, 100% { transform: translateX(0) scaleY(1); }
  25% { transform: translateX(3px) scaleY(1.15); }
  50% { transform: translateX(-2px) scaleY(0.9); }
  75% { transform: translateX(4px) scaleY(1.1); }
}

@keyframes bubbleRise {
  0% { transform: translateY(0) scale(0.8); opacity: 0.8; }
  100% { transform: translateY(-90px) scale(1.3); opacity: 0; }
}

@keyframes neonPulse {
  0%, 100% { filter: brightness(1) drop-shadow(0 0 8px currentColor); }
  50% { filter: brightness(1.3) drop-shadow(0 0 18px currentColor); }
}

@keyframes shimmerGold {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

@keyframes glowBreathe {
  0%, 100% { box-shadow: 0 0 12px rgba(0,229,255,0.3), inset 0 0 8px rgba(0,229,255,0.15); }
  50% { box-shadow: 0 0 28px rgba(0,229,255,0.6), inset 0 0 18px rgba(0,229,255,0.35); }
}

.vaayu-float3d { animation: float3D 6s ease-in-out infinite; }
.vaayu-float3d-reverse { animation: float3DReverse 6s ease-in-out infinite; }
.vaayu-float3d-fast { animation: float3D 4s ease-in-out infinite; }
.vaayu-flame-pulse { animation: flamePulse 4s ease-in-out infinite; }
.vaayu-wave { animation: waveMeniscus 3s ease-in-out infinite; }
.vaayu-bubble { animation: bubbleRise 3.5s ease-in infinite; }
.vaayu-bubble-d1 { animation: bubbleRise 2.8s ease-in 0.3s infinite; }
.vaayu-bubble-d2 { animation: bubbleRise 3.2s ease-in 0.7s infinite; }
.vaayu-bubble-d3 { animation: bubbleRise 4s ease-in 1.1s infinite; }
.vaayu-bubble-d4 { animation: bubbleRise 3s ease-in 1.5s infinite; }
.vaayu-bubble-d5 { animation: bubbleRise 3.8s ease-in 0.5s infinite; }
.vaayu-neon-pulse { animation: neonPulse 2.5s ease-in-out infinite; }
.vaayu-glow-breathe { animation: glowBreathe 3s ease-in-out infinite; }
.vaayu-shimmer-gold {
  background-size: 200% 100%;
  animation: shimmerGold 3s linear infinite;
}
`;

export function useVaayu3DAnimations() {
  useEffect(() => {
    if (Platform.OS !== 'web') return;
    if (document.getElementById(GLOBAL_STYLE_ID)) return;
    const style = document.createElement('style');
    style.id = GLOBAL_STYLE_ID;
    style.textContent = CSS;
    document.head.appendChild(style);
  }, []);
}

export default useVaayu3DAnimations;
