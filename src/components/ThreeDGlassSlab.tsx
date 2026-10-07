import '../polyfills';
import React, { useRef } from 'react';
import { Canvas } from '@react-three/fiber';
import { RoundedBox, MeshTransmissionMaterial, Float, Environment, Lightformer } from '@react-three/drei';
import * as THREE from 'three';

export default function ThreeDGlassSlab({ color = '#00E5FF', tilt = [0, 0, 0] as [number, number, number] }) {
  return (
    <Canvas camera={{ position: [0, 0, 8], fov: 40 }} style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', zIndex: 0, pointerEvents: 'none' }} gl={{ alpha: true, antialias: true }}>
      <ambientLight intensity={1.5} />
      <directionalLight position={[10, 10, 10]} intensity={3} color={color} />
      
      <Environment resolution={256}>
        <group rotation={[-Math.PI / 2, 0, 0]}>
          <Lightformer intensity={4} form="rect" color="white" position={[0, 5, -2]} scale={[20, 10, 1]} />
          <Lightformer intensity={2} form="rect" color={color} position={[0, 5, 2]} scale={[20, 10, 1]} />
        </group>
      </Environment>

      <Float speed={2} rotationIntensity={0.3} floatIntensity={0.5}>
        {/* Adjusted scale for tablet proportion */}
        <RoundedBox args={[6, 8.5, 0.4]} radius={0.3} rotation={tilt}>
          <MeshTransmissionMaterial
            backside
            samples={6}
            thickness={1}
            roughness={0.1}
            chromaticAberration={0.03}
            anisotropy={0.1}
            distortion={0.1}
            distortionScale={0.3}
            temporalDistortion={0.1}
            clearcoat={1}
            clearcoatRoughness={0.1}
            color={color}
            emissive={color}
            emissiveIntensity={0.2}
          />
        </RoundedBox>
      </Float>
    </Canvas>
  );
}
