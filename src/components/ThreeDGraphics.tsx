import React from 'react';
import { View } from 'react-native';
import Svg, { Circle, Defs, Ellipse, FeGaussianBlur, FeMerge, FeMergeNode, Filter, G, LinearGradient, Path, RadialGradient, Rect, Stop, Text as SvgText } from 'react-native-svg';

export const BlueFlameOrb3D = ({ percentage }: { percentage: number | string }) => (
  <View style={{ width: 240, height: 240, justifyContent: 'center', alignItems: 'center' }}>
    <Svg width="240" height="240" viewBox="0 0 240 240">
      <Defs>
        <RadialGradient id="plasmaCore" cx="50%" cy="50%" r="50%">
          <Stop offset="0%" stopColor="#041E42" />
          <Stop offset="65%" stopColor="#0284C7" />
          <Stop offset="88%" stopColor="#00E5FF" />
          <Stop offset="100%" stopColor="transparent" />
        </RadialGradient>
        <LinearGradient id="fireGrad" x1="0%" y1="100%" x2="100%" y2="0%">
          <Stop offset="0%" stopColor="#0284C7" />
          <Stop offset="50%" stopColor="#00E5FF" />
          <Stop offset="100%" stopColor="#E0F2FE" />
        </LinearGradient>
        <Filter id="blueBloom" x="-30%" y="-30%" width="160%" height="160%">
          <FeGaussianBlur stdDeviation="8" result="blur" />
          <FeMerge>
            <FeMergeNode in="blur" />
            <FeMergeNode in="SourceGraphic" />
          </FeMerge>
        </Filter>
      </Defs>

      {/* Concentric glowing rings */}
      <Circle cx="120" cy="120" r="95" stroke="url(#fireGrad)" strokeWidth="3" filter="url(#blueBloom)" strokeDasharray="45 12 25 8" strokeLinecap="round" fill="none" opacity="0.6" />
      <Circle cx="120" cy="120" r="86" stroke="url(#fireGrad)" strokeWidth="2" filter="url(#blueBloom)" strokeDasharray="30 15" strokeLinecap="round" fill="none" opacity="0.8" />
      <Circle cx="120" cy="120" r="78" stroke="url(#fireGrad)" strokeWidth="4" filter="url(#blueBloom)" strokeDasharray="60 20" strokeLinecap="round" fill="none" opacity="0.9" />

      {/* 16 organic curved flame petals */}
      <G filter="url(#blueBloom)">
        {[0, 22.5, 45, 67.5, 90, 112.5, 135, 157.5, 180, 202.5, 225, 247.5, 270, 292.5, 315, 337.5].map((deg) => (
          <Path 
            key={deg}
            d="M120,12 C132,25 128,38 120,44 C112,38 108,25 120,12 Z" 
            fill="url(#fireGrad)" 
            transform={`rotate(${deg} 120 120)`} 
            opacity="0.85" 
          />
        ))}
      </G>

      {/* Dark Glossy Inner Sphere */}
      <Circle cx="120" cy="120" r="72" fill="url(#plasmaCore)" />

      {/* Center Text */}
      <SvgText x="120" y="125" fill="#FFFFFF" fontSize="34" fontWeight="900" textAnchor="middle">{percentage}</SvgText>
      <SvgText x="120" y="150" fill="#7DD3FC" fontSize="14" fontWeight="900" textAnchor="middle" letterSpacing="2">RECOVERY</SvgText>
    </Svg>
  </View>
);

export const LiquidBloodCapsule3D = ({ group, count }: { group: string, count: number }) => {
  const maxCapacity = 50;
  const fillPercent = Math.min(100, Math.max(15, (count / maxCapacity) * 100));
  const fillHeight = (fillPercent / 100) * 140; 
  const liquidTopY = 180 - fillHeight;

  return (
    <View style={{ alignItems: 'center' }}>
      <Svg width="110" height="195" viewBox="0 0 110 195">
        <Defs>
          <LinearGradient id="glassTube" x1="0" y1="0" x2="1" y2="0">
            <Stop offset="0%" stopColor="#FFFFFF" stopOpacity="0.3" />
            <Stop offset="15%" stopColor="#94A3B8" stopOpacity="0.1" />
            <Stop offset="85%" stopColor="#0F172A" stopOpacity="0.4" />
            <Stop offset="100%" stopColor="#00E5FF" stopOpacity="0.3" />
          </LinearGradient>
          <LinearGradient id="bloodLiquid" x1="0" y1="0" x2="1" y2="0">
            <Stop offset="0%" stopColor="#FF4D6D" />
            <Stop offset="40%" stopColor="#E11D48" />
            <Stop offset="80%" stopColor="#9F1239" />
            <Stop offset="100%" stopColor="#4C0519" />
          </LinearGradient>
        </Defs>

        {/* Outer 3D rounded glass tube */}
        <Rect x="4" y="4" width="102" height="187" rx="51" fill="url(#glassTube)" stroke="rgba(255,255,255,0.45)" strokeWidth="2.5" />
        
        {/* Bright white curved glass reflection arc */}
        <Path d="M 22 50 A 38 38 0 0 1 55 14" stroke="rgba(255,255,255,0.65)" strokeWidth="6" strokeLinecap="round" fill="none" />

        {/* Glowing 3D ruby-red liquid fill */}
        <G>
          {/* Main rectangular fill with rounded bottom */}
          <Path d={`M 7 ${liquidTopY} L 103 ${liquidTopY} L 103 144 A 48 48 0 0 1 7 144 Z`} fill="url(#bloodLiquid)" />
          {/* Top Elliptical Meniscus */}
          <Ellipse cx="55" cy={liquidTopY} rx="48" ry="10" fill="#FF4D6D" />
          
          {/* Glowing micro-bubbles */}
          <Circle cx="35" cy={liquidTopY + 25} r="4" fill="rgba(255,180,200,0.6)" />
          <Circle cx="75" cy={liquidTopY + 45} r="3" fill="rgba(255,180,200,0.6)" />
          <Circle cx="50" cy={liquidTopY + 70} r="5" fill="rgba(255,180,200,0.6)" />
          <Circle cx="80" cy={liquidTopY + 90} r="2.5" fill="rgba(255,180,200,0.6)" />
          <Circle cx="25" cy={liquidTopY + 105} r="3.5" fill="rgba(255,180,200,0.6)" />
        </G>

        {/* Text Overlays */}
        <SvgText x="55" y={liquidTopY + (fillHeight / 2) - 5} fill="#FFFFFF" fontSize="26" fontWeight="bold" textAnchor="middle">{group}</SvgText>
        <SvgText x="55" y={liquidTopY + (fillHeight / 2) + 18} fill="#FFFFFF" fontSize="14" fontWeight="bold" textAnchor="middle">{count} Units</SvgText>
      </Svg>
    </View>
  );
};

export const HologramAvatar3D = () => (
  <View style={{ width: 140, height: 140, justifyContent: 'center', alignItems: 'center' }}>
    <Svg width="140" height="140" viewBox="0 0 160 160">
      <Defs>
        <RadialGradient id="ringGlow" cx="50%" cy="50%" r="50%">
          <Stop offset="80%" stopColor="#00E5FF" stopOpacity="0" />
          <Stop offset="95%" stopColor="#00E5FF" stopOpacity="0.8" />
          <Stop offset="100%" stopColor="#00E5FF" stopOpacity="0" />
        </RadialGradient>
        <LinearGradient id="holoBody" x1="0" y1="0" x2="0" y2="1">
          <Stop offset="0%" stopColor="#E0FFFF" stopOpacity="0.9" />
          <Stop offset="50%" stopColor="#00E5FF" stopOpacity="0.6" />
          <Stop offset="100%" stopColor="#0284C7" stopOpacity="0" />
        </LinearGradient>
      </Defs>
      
      {/* 3 Glowing Cyan Ellipse Hologram Projection Rings */}
      <Ellipse cx="80" cy="140" rx="70" ry="18" fill="url(#ringGlow)" stroke="#7DF9FF" strokeWidth="1.5" opacity="0.9" />
      <Ellipse cx="80" cy="132" rx="55" ry="14" fill="none" stroke="#00E5FF" strokeWidth="2" opacity="0.7" />
      <Ellipse cx="80" cy="124" rx="42" ry="10" fill="none" stroke="#0284C7" strokeWidth="3" opacity="0.5" />
      
      {/* Avatar Bust */}
      <Circle cx="80" cy="65" r="22" fill="url(#holoBody)" />
      <Path d="M 35 140 C 35 105, 60 95, 80 95 C 100 95, 125 105, 125 140 Z" fill="url(#holoBody)" />
      
      {/* Scanlines */}
      <Path d="M 50 65 L 110 65 M 40 85 L 120 85 M 35 105 L 125 105 M 35 125 L 125 125" stroke="#E0FFFF" strokeWidth="1" opacity="0.3" />
    </Svg>
  </View>
);

export const GoldShield3D = () => (
  <View style={{ width: 140, height: 140, justifyContent: 'center', alignItems: 'center' }}>
    <Svg width="140" height="140" viewBox="0 0 160 160">
      <Defs>
        <LinearGradient id="shieldGoldMain" x1="0" y1="0" x2="1" y2="1">
          <Stop offset="0%" stopColor="#FEF08A" />
          <Stop offset="30%" stopColor="#F59E0B" />
          <Stop offset="70%" stopColor="#B45309" />
          <Stop offset="100%" stopColor="#78350F" />
        </LinearGradient>
        <LinearGradient id="shieldGoldHighlight" x1="0" y1="0" x2="1" y2="0">
          <Stop offset="0%" stopColor="#FEF08A" stopOpacity="0.9" />
          <Stop offset="100%" stopColor="#F59E0B" stopOpacity="0" />
        </LinearGradient>
        <LinearGradient id="shieldGoldDark" x1="0" y1="0" x2="1" y2="0">
          <Stop offset="0%" stopColor="#78350F" stopOpacity="0" />
          <Stop offset="100%" stopColor="#451A03" stopOpacity="0.8" />
        </LinearGradient>
      </Defs>
      {/* Base Shield */}
      <Path d="M 80 15 L 25 35 L 25 80 C 25 125, 80 155, 80 155 C 80 155, 135 125, 135 80 L 135 35 Z" fill="url(#shieldGoldMain)" stroke="#FDE047" strokeWidth="3" strokeLinejoin="round" />
      
      {/* Left Facet Highlight */}
      <Path d="M 80 15 L 25 35 L 25 80 C 25 125, 80 155, 80 155 Z" fill="url(#shieldGoldHighlight)" />
      
      {/* Right Facet Shadow */}
      <Path d="M 80 15 L 135 35 L 135 80 C 135 125, 80 155, 80 155 Z" fill="url(#shieldGoldDark)" />
      
      {/* Inner Facet Lines */}
      <Path d="M 80 15 L 80 155 M 25 35 L 135 35" stroke="#FEF08A" strokeWidth="2.5" opacity="0.6" />
      
      {/* Center Emblem */}
      <Circle cx="80" cy="80" r="22" fill="#0F172A" stroke="#FDE047" strokeWidth="2" />
      <Path d="M 80 62 L 80 98 M 62 80 L 98 80" stroke="#FDE047" strokeWidth="3" />
    </Svg>
  </View>
);

export const GoldMicrochip3D = () => (
  <View style={{ width: 46, height: 36, justifyContent: 'center', alignItems: 'center' }}>
    <Svg width="46" height="36" viewBox="0 0 46 36">
      <Defs>
        <LinearGradient id="chipGold" x1="0" y1="0" x2="1" y2="1">
          <Stop offset="0%" stopColor="#FEF08A" />
          <Stop offset="50%" stopColor="#F59E0B" />
          <Stop offset="100%" stopColor="#B45309" />
        </LinearGradient>
      </Defs>
      <Rect x="0" y="0" width="46" height="36" rx="6" fill="url(#chipGold)" stroke="#78350F" strokeWidth="1" />
      <Path d="M 12 0 L 12 36 M 34 0 L 34 36 M 0 18 L 46 18 M 12 8 L 0 8 M 12 28 L 0 28 M 34 8 L 46 8 M 34 28 L 46 28" stroke="#92400E" strokeWidth="1.5" opacity="0.7" />
    </Svg>
  </View>
);
