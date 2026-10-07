import '../polyfills';
import React from 'react';
import { Canvas } from '@react-three/fiber';
import { Sphere, MeshDistortMaterial, Float, Environment } from '@react-three/drei';
import * as THREE from 'three';

export default function ThreeDBlueOrb() {
  return (
    <Canvas camera={{ position: [0, 0, 5], fov: 45 }} style={{ width: 340, height: 340, position: 'absolute', top: 0, left: 0, zIndex: 0, pointerEvents: 'none' }} gl={{ alpha: true, antialias: true }}>
      <ambientLight intensity={1} />
      <directionalLight position={[10, 10, 5]} intensity={3} color="#00E5FF" />
      <pointLight position={[-10, -10, -5]} intensity={2} color="#38BDF8" />
      
      <Float speed={2.5} rotationIntensity={2} floatIntensity={1.5}>
        {/* Outer Plasma Aura */}
        <Sphere args={[1.5, 64, 64]}>
          <MeshDistortMaterial
            color="#00E5FF"
            emissive="#00E5FF"
            emissiveIntensity={1.5}
            roughness={0.1}
            metalness={0.8}
            distort={0.4}
            speed={5}
            transparent
            opacity={0.6}
            side={THREE.DoubleSide}
            blending={THREE.AdditiveBlending}
          />
        </Sphere>
        
        {/* Inner Core */}
        <Sphere args={[1.1, 32, 32]}>
          <MeshDistortMaterial
            color="#FFFFFF"
            emissive="#FFFFFF"
            emissiveIntensity={2}
            roughness={0.2}
            metalness={0.2}
            distort={0.2}
            speed={3}
            transparent
            opacity={0.9}
          />
        </Sphere>
      </Float>
    </Canvas>
  );
}
