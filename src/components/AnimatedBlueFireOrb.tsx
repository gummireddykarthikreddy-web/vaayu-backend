import React, { useEffect, useRef } from 'react';

export default function AnimatedBlueFireOrb() {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    let particles: any[] = [];
    let animationFrameId: number;

    const createParticle = () => {
      // Spawn particles near the center/bottom to shoot upwards
      const angle = Math.random() * Math.PI * 2;
      const radius = Math.random() * 80; // Inner ring
      return {
        x: 170 + Math.cos(angle) * radius,
        y: 200 + Math.sin(angle) * radius,
        vx: (Math.random() - 0.5) * 2,
        vy: -Math.random() * 5 - 2, // Shoot upwards fast!
        life: 1,
        size: Math.random() * 8 + 4,
        hue: 180 + Math.random() * 30, // Cyan to blue
      };
    };

    for (let i = 0; i < 150; i++) particles.push(createParticle());

    const render = () => {
      ctx.clearRect(0, 0, 340, 340);
      ctx.globalCompositeOperation = 'lighter';

      particles.forEach((p, index) => {
        p.x += p.vx;
        p.y += p.vy;
        p.life -= 0.015;
        p.size *= 0.95; // Shrink as they rise

        if (p.life <= 0) {
          particles[index] = createParticle();
        }

        ctx.beginPath();
        // Elongated flame particles
        ctx.ellipse(p.x, p.y, p.size, p.size * 2, 0, 0, Math.PI * 2);
        ctx.fillStyle = `hsla(${p.hue}, 100%, 60%, ${p.life})`;
        ctx.shadowBlur = 15;
        ctx.shadowColor = `hsla(${p.hue}, 100%, 50%, ${p.life})`;
        ctx.fill();
      });

      animationFrameId = requestAnimationFrame(render);
    };

    render();

    return () => cancelAnimationFrame(animationFrameId);
  }, []);

  return (
    <canvas 
      ref={canvasRef} 
      width={340} 
      height={340} 
      style={{ 
        position: 'absolute', 
        top: -40, 
        left: -30, 
        zIndex: 5, 
        pointerEvents: 'none',
        filter: 'contrast(1.5) brightness(1.2)'
      }} 
    />
  );
}
