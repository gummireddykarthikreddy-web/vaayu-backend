import os

explore_content = """import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, Image } from 'react-native';
import { useRouter } from 'expo-router';
import AnimatedBlueFireOrb from '../components/AnimatedBlueFireOrb';

const CrimsonGlassSlab = require('../../assets/images/CrimsonGlassSlab.jpg');
const ObsidianGoldSlab = require('../../assets/images/ObsidianGoldSlab.jpg');
const BurningBlueFireOrb = require('../../assets/images/BurningBlueFireOrb.jpg');
const GlassCardSlab = require('../../assets/images/GlassCardSlab.jpg');

const getUri = (source: any): string => {
  if (!source) return '';
  if (typeof source === 'string') return source;
  if (typeof source === 'object') return source.uri || source.default || '';
  return String(source);
};

export default function DoctorVaultScreen() {
  const router = useRouter();
  const [patientData, setPatientData] = useState<any>(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/patient/VHP-88390')
      .then(res => res.json())
      .then(data => setPatientData(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <style>{`
        @keyframes fireSpin {
          0% { transform: rotate(0deg) scale(1); filter: brightness(1.2) contrast(1.3); }
          50% { transform: rotate(180deg) scale(1.05); filter: brightness(1.5) contrast(1.5); }
          100% { transform: rotate(360deg) scale(1); filter: brightness(1.2) contrast(1.3); }
        }
        @keyframes float3D {
          0%, 100% { transform: perspective(1000px) rotateY(15deg) rotateX(10deg) translateY(0px); }
          50% { transform: perspective(1000px) rotateY(12deg) rotateX(8deg) translateY(-15px); }
        }
        @keyframes float3DRight {
          0%, 100% { transform: perspective(1000px) rotateY(-15deg) rotateX(10deg) translateY(0px); }
          50% { transform: perspective(1000px) rotateY(-12deg) rotateX(8deg) translateY(-15px); }
        }
        @keyframes pulseGlow {
          0%, 100% { filter: drop-shadow(0 0 20px rgba(255,42,95,0.4)); }
          50% { filter: drop-shadow(0 0 40px rgba(255,42,95,0.8)); }
        }
      `}</style>

      <TouchableOpacity style={styles.backBtn} onPress={() => router.back()}>
        <Text style={styles.backBtnText}>← BACK TO HUB</Text>
      </TouchableOpacity>

      {patientData && (
        <View style={styles.mainGrid}>
          {/* ROW 1 */}
          <View style={styles.row}>
            {/* 3D Crimson Glass */}
            <View style={styles.gridCell}>
              <Text style={styles.panelLabelTop}>3D Crimson Glass</Text>
              <div style={{ animation: 'float3D 6s ease-in-out infinite, pulseGlow 4s infinite', width: '100%', height: 480, position: 'relative', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
                <img src={getUri(CrimsonGlassSlab)} style={{ position: 'absolute', width: '100%', height: '100%', objectFit: 'contain', mixBlendMode: 'screen' }} />
                
                {/* Embedded UI over Crimson Glass */}
                <div style={{ position: 'absolute', width: '75%', height: '80%', zIndex: 10, display: 'flex', flexDirection: 'column', padding: 20 }}>
                  <Text style={{ color: '#FFFFFF', fontSize: 24, fontWeight: '900', textShadowColor: '#FF2A5F', textShadowOffset: {width: 0, height: 0}, textShadowRadius: 10, marginBottom: 20, lineHeight: 30 }}>Pre-Surgery Safety &{`\n`}Infection Shield</Text>
                  
                  <View style={{ backgroundColor: 'rgba(0,0,0,0.4)', borderRadius: 12, padding: 15, borderWidth: 1, borderColor: 'rgba(255,100,100,0.3)', marginBottom: 15 }}>
                    <Text style={{ color: '#E2E8F0', fontSize: 13, fontWeight: 'bold', marginBottom: 10 }}>Infection Risks</Text>
                    <View style={{ flexDirection: 'row', justifyContent: 'space-between', paddingHorizontal: 10 }}>
                      {[85, 85, 85].map((val, i) => (
                        <div key={i} style={{ width: 44, height: 44, borderRadius: 22, border: '2px solid #FF2A5F', display: 'flex', justifyContent: 'center', alignItems: 'center', boxShadow: '0 0 10px rgba(255,42,95,0.5)' }}>
                          <Text style={{ color: '#FFF', fontWeight: 'bold', fontSize: 12 }}>{val}%</Text>
                        </div>
                      ))}
                    </View>
                  </View>

                  <View style={{ flexDirection: 'row', gap: 10, flex: 1 }}>
                    <View style={{ flex: 1, backgroundColor: 'rgba(0,0,0,0.4)', borderRadius: 12, padding: 12, borderWidth: 1, borderColor: 'rgba(255,100,100,0.3)' }}>
                      <Text style={{ color: '#E2E8F0', fontSize: 11, fontWeight: 'bold', marginBottom: 10 }}>Safety Protocols</Text>
                      <Text style={{ color: '#94A3B8', fontSize: 10, marginBottom: 4 }}>✔ Validate Protocol</Text>
                      <Text style={{ color: '#94A3B8', fontSize: 10, marginBottom: 4 }}>✔ Sterilize Tools</Text>
                    </View>
                    <View style={{ flex: 1, backgroundColor: 'rgba(0,0,0,0.4)', borderRadius: 12, padding: 12, borderWidth: 1, borderColor: 'rgba(255,100,100,0.3)' }}>
                      <Text style={{ color: '#E2E8F0', fontSize: 11, fontWeight: 'bold', marginBottom: 10 }}>Patient Vitals</Text>
                      <div style={{ height: 4, backgroundColor: '#334', borderRadius: 2, marginBottom: 10 }}><div style={{ width: '80%', height: '100%', backgroundColor: '#FF2A5F' }} /></div>
                      <div style={{ height: 4, backgroundColor: '#334', borderRadius: 2 }}><div style={{ width: '60%', height: '100%', backgroundColor: '#00E5FF' }} /></div>
                    </View>
                  </View>

                  <Text style={{ color: '#FF2A5F', fontSize: 16, fontWeight: '900', marginTop: 15 }}>Alert Status: High  ⚠️</Text>
                </div>
              </div>
            </View>

            {/* 3D Obsidian & Gold checklist */}
            <View style={styles.gridCell}>
              <Text style={styles.panelLabelTop}>3D Obsidian & Gold checklist</Text>
              <div style={{ animation: 'float3DRight 7s ease-in-out infinite', width: '100%', height: 480, position: 'relative', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
                <img src={getUri(ObsidianGoldSlab)} style={{ position: 'absolute', width: '100%', height: '100%', objectFit: 'contain', mixBlendMode: 'screen' }} />
                
                {/* Embedded UI over Obsidian Slab */}
                <div style={{ position: 'absolute', width: '70%', height: '70%', zIndex: 10, display: 'flex', flexDirection: 'column', padding: 20 }}>
                  <Text style={{ color: '#FFFFFF', fontSize: 20, fontWeight: '900', textShadowColor: '#F59E0B', textShadowOffset: {width: 0, height: 0}, textShadowRadius: 10, marginBottom: 20, lineHeight: 28, textAlign: 'center' }}>Doctor's Pre-Surgery{`\n`}Preventive Measures</Text>
                  
                  <View style={{ gap: 12, flex: 1 }}>
                    {['Verify Patient Identity', 'Confirm Surgical Site', 'Review Medical History', 'Administer Prophylactic Antibiotics', 'Check Equipment Functionality'].map((task, i) => (
                      <View key={i} style={{ flexDirection: 'row', alignItems: 'center', backgroundColor: 'rgba(0,0,0,0.5)', padding: 12, borderRadius: 8, borderWidth: 1, borderColor: '#F59E0B40' }}>
                        <div style={{ width: 18, height: 18, borderRadius: 9, backgroundColor: '#F59E0B', display: 'flex', justifyContent: 'center', alignItems: 'center', marginRight: 10 }}><Text style={{ color: '#000', fontSize: 10, fontWeight: 'bold' }}>✓</Text></div>
                        <Text style={{ color: '#E2E8F0', fontSize: 11, fontWeight: 'bold' }}>{task}</Text>
                      </View>
                    ))}
                  </View>
                  <div style={{ width: '100%', height: 4, backgroundColor: 'rgba(255,255,255,0.1)', borderRadius: 2, marginTop: 20 }}>
                    <div style={{ width: '80%', height: '100%', backgroundColor: '#F59E0B', boxShadow: '0 0 10px #F59E0B' }} />
                  </div>
                  <Text style={{ color: '#E2E8F0', textAlign: 'right', marginTop: 5, fontSize: 11, fontWeight: 'bold' }}>80%</Text>
                </div>
              </div>
            </View>
          </View>

          {/* ROW 2 */}
          <View style={[styles.row, { marginTop: 40 }]}>
            
            {/* 3D Blue Flame Recovery Orb */}
            <View style={styles.gridCell}>
              <div style={{ position: 'relative', width: '100%', height: 400, display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
                <img 
                  src={getUri(BurningBlueFireOrb)} 
                  style={{ position: 'absolute', width: 500, height: 500, objectFit: 'contain', mixBlendMode: 'screen', animation: 'fireSpin 12s linear infinite', pointerEvents: 'none' }} 
                />
                <AnimatedBlueFireOrb />
                
                <View style={[styles.orbTextLayer, { zIndex: 10 }]}>
                  <Text style={styles.orbPercent}>{patientData?.recovery_insights?.recovery_rate || 92}%</Text>
                  <Text style={styles.orbLabel}>Recovery Index</Text>
                </View>

                {/* Corner Labels matching image */}
                <Text style={[styles.cornerLabel, { top: 20, left: 20 }]}>Post-Op Vital{`\n`}Monitoring</Text>
                <Text style={[styles.cornerLabel, { top: 20, right: 20 }]}>Healing Orb{`\n`}Steness</Text>
                <Text style={[styles.cornerLabel, { bottom: 20, left: 20 }]}>Post-Op Vital{`\n`}Monitoring</Text>
                <Text style={[styles.cornerLabel, { bottom: 20, right: 20 }]}>Healing{`\n`}Progress</Text>
              </div>
              <Text style={[styles.panelLabelBottom, { marginTop: -20 }]}>3D Blue Flame Recovery Orb</Text>
            </View>

            {/* AI Clinical Summary + Composer */}
            <View style={styles.gridCell}>
              <div style={{ width: '100%', height: 380, position: 'relative', padding: 20 }}>
                <img src={getUri(GlassCardSlab)} style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', borderRadius: 20, opacity: 0.2 }} />
                
                <View style={{ backgroundColor: 'rgba(30,41,59,0.8)', borderRadius: 16, padding: 20, borderWidth: 1, borderColor: 'rgba(255,255,255,0.1)', marginBottom: 20 }}>
                  <Text style={{ color: '#FFF', fontSize: 16, fontWeight: 'bold', marginBottom: 10 }}>AI Clinical Summary</Text>
                  <Text style={{ color: '#94A3B8', fontSize: 11, marginBottom: 15 }}>Synthesized key data points for realms and recommendations.</Text>
                  <View style={{ flexDirection: 'row', gap: 20 }}>
                    <View style={{ flex: 1 }}>
                      <Text style={styles.bulletText}>• Synthesized key Asta points</Text>
                      <Text style={styles.bulletText}>• Confirmed Medical History</Text>
                    </View>
                    <View style={{ flex: 1 }}>
                      <Text style={styles.bulletText}>• Recommendations preserving surgical trio</Text>
                      <Text style={styles.bulletText}>• Recommendations recovery prevention</Text>
                    </View>
                  </View>
                </View>

                <View style={{ backgroundColor: 'rgba(30,41,59,0.8)', borderRadius: 16, padding: 20, borderWidth: 1, borderColor: 'rgba(255,255,255,0.1)' }}>
                  <View style={{ flexDirection: 'row', justifyContent: 'space-between', marginBottom: 15 }}>
                    <Text style={{ color: '#FFF', fontSize: 16, fontWeight: 'bold' }}>3D Prescription Composer</Text>
                    <View style={{ backgroundColor: 'rgba(255,255,255,0.1)', paddingHorizontal: 10, paddingVertical: 4, borderRadius: 20 }}><Text style={{ color: '#FFF', fontSize: 10 }}>Select category</Text></View>
                  </View>
                  
                  <View style={{ flexDirection: 'row', justifyContent: 'space-between', marginBottom: 20 }}>
                    {['Pain Mgt', 'Antibiotics', 'Anti-inflam', 'Recovery', 'Specialized'].map((cat, i) => {
                      const colors = ['#F43F5E', '#3B82F6', '#F97316', '#10B981', '#8B5CF6'];
                      return (
                        <View key={i} style={{ alignItems: 'center' }}>
                          <View style={{ width: 40, height: 40, borderRadius: 12, backgroundColor: colors[i] + '40', marginBottom: 8, borderWidth: 1, borderColor: colors[i] }} />
                          <Text style={{ color: '#94A3B8', fontSize: 9 }}>{cat}</Text>
                        </View>
                      );
                    })}
                  </View>

                  <View style={{ backgroundColor: 'rgba(0,0,0,0.4)', borderRadius: 12, padding: 15, alignItems: 'center' }}>
                    <Text style={{ color: '#FFF', fontSize: 14, fontWeight: 'bold', marginBottom: 5 }}>Vault Composer</Text>
                    <Text style={{ color: '#94A3B8', fontSize: 10 }}>Drag and drop items into a central area.</Text>
                  </View>
                </View>

              </div>
              <Text style={[styles.panelLabelBottom, { textAlign: 'center', marginTop: 10 }]}>AI Clinical Summary + 5-Category{`\n`}3D Prescription & Vault Composer</Text>
            </View>

          </View>
        </View>
      )}
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: { flexGrow: 1, backgroundColor: '#09111E', padding: 40 },
  backBtn: { alignSelf: 'flex-start', marginBottom: 20, padding: 10, backgroundColor: 'rgba(0, 229, 255, 0.1)', borderRadius: 8, borderWidth: 1, borderColor: '#00E5FF', zIndex: 50 },
  backBtnText: { color: '#00E5FF', fontWeight: 'bold' },
  
  mainGrid: { maxWidth: 1200, width: '100%', alignSelf: 'center', flexDirection: 'column' },
  row: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', gap: 40 },
  gridCell: { flex: 1, alignItems: 'center' },

  panelLabelTop: { color: '#FFFFFF', fontSize: 20, fontWeight: '900', marginBottom: 20, letterSpacing: 1 },
  panelLabelBottom: { color: '#FFFFFF', fontSize: 20, fontWeight: '900', marginTop: 20, letterSpacing: 1, textAlign: 'center' },
  
  orbTextLayer: { position: 'absolute', justifyContent: 'center', alignItems: 'center' },
  orbPercent: { color: '#FFFFFF', fontSize: 52, fontWeight: '900', textShadowColor: '#00E5FF', textShadowOffset: { width: 0, height: 0 }, textShadowRadius: 20 },
  orbLabel: { color: '#E2E8F0', fontSize: 14, fontWeight: '900', letterSpacing: 1, marginTop: 5 },
  cornerLabel: { position: 'absolute', color: '#94A3B8', fontSize: 12, letterSpacing: 0.5 },
  bulletText: { color: '#E2E8F0', fontSize: 10, marginBottom: 8, lineHeight: 14 }
});
"""

open('src/app/explore.tsx', 'w', encoding='utf-8').write(explore_content)

index_content = """import React from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity } from 'react-native';
import { useRouter } from 'expo-router';

const HologramAvatarImg = require('../../assets/images/HologramAvatar.jpg');
const GoldShieldImg = require('../../assets/images/GoldShield.jpg');

const getUri = (source: any): string => {
  if (!source) return '';
  if (typeof source === 'string') return source;
  if (typeof source === 'object') return source.uri || source.default || '';
  return String(source);
};

export default function IndexHub() {
  const router = useRouter();

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <style>{`
        @keyframes holoFloat {
          0%, 100% { transform: translateY(0px) scale(1.05); filter: brightness(1.3) contrast(1.4) drop-shadow(0 0 20px #00E5FF); }
          50% { transform: translateY(-12px) scale(1.12); filter: brightness(1.6) contrast(1.5) drop-shadow(0 0 35px #38BDF8); }
        }
        @keyframes shieldFloat {
          0%, 100% { transform: translateY(0px) scale(1.05); filter: brightness(1.3) contrast(1.4) drop-shadow(0 0 20px #F59E0B); }
          50% { transform: translateY(-12px) scale(1.12); filter: brightness(1.6) contrast(1.5) drop-shadow(0 0 35px #FDE047); }
        }
        .hub-banner {
          background: linear-gradient(180deg, rgba(30,41,59,0.8) 0%, rgba(15,23,42,0.95) 100%);
          border: 1px solid rgba(255,255,255,0.1);
          box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }
        .hero-left {
          background: linear-gradient(180deg, rgba(56,189,248,0.2) 0%, rgba(15,23,42,0.9) 100%);
          border: 1px solid rgba(56,189,248,0.3);
          box-shadow: 0 20px 40px rgba(0,0,0,0.6), inset 0 2px 20px rgba(56,189,248,0.2);
        }
        .hero-right {
          background: linear-gradient(180deg, rgba(245,158,11,0.15) 0%, rgba(15,23,42,0.9) 100%);
          border: 1px solid rgba(245,158,11,0.3);
          box-shadow: 0 20px 40px rgba(0,0,0,0.6), inset 0 2px 20px rgba(245,158,11,0.15);
        }
      `}</style>

      {/* Top Banner */}
      <div className="hub-banner" style={{ width: '100%', maxWidth: 1100, borderRadius: 16, padding: '25px 40px', display: 'flex', justifyContent: 'center', alignItems: 'center', marginBottom: 40 }}>
        <Text style={{ fontSize: 28, fontWeight: '900', color: '#FFFFFF', textAlign: 'center', letterSpacing: 0.5 }}>
          Welcome to Vaayu — National 3D Cellular{`\n`}Recovery & Surgical Ecosystem
        </Text>
      </div>

      <View style={{ maxWidth: 1100, width: '100%', gap: 30 }}>
        
        {/* ROW 1: Two Huge Slabs */}
        <View style={{ flexDirection: 'row', gap: 30, height: 320 }}>
          <TouchableOpacity style={{ flex: 1 }} onPress={() => router.push('/patient')}>
            <div className="hero-left" style={{ flex: 1, height: '100%', borderRadius: 24, borderBottomWidth: 12, borderBottomStyle: 'solid', borderBottomColor: 'rgba(56,189,248,0.2)', padding: 35, display: 'flex', flexDirection: 'row', justifyContent: 'space-between' }}>
              <View style={{ flex: 1 }}>
                <Text style={{ color: '#FFF', fontSize: 32, fontWeight: '900', lineHeight: 40, marginBottom: 15, textShadowColor: '#38BDF8', textShadowOffset: {width:0, height:0}, textShadowRadius: 10 }}>Vaayu Patient{`\n`}Portal &{`\n`}NutriMed</Text>
                <Text style={{ color: '#94A3B8', fontSize: 14 }}>3D hologram hologram</Text>
              </View>
              <img src={getUri(HologramAvatarImg)} style={{ width: 140, height: 140, objectFit: 'contain', mixBlendMode: 'screen', animation: 'holoFloat 4s ease-in-out infinite' }} />
            </div>
          </TouchableOpacity>

          <TouchableOpacity style={{ flex: 1 }} onPress={() => router.push('/explore')}>
            <div className="hero-right" style={{ flex: 1, height: '100%', borderRadius: 24, borderBottomWidth: 12, borderBottomStyle: 'solid', borderBottomColor: 'rgba(245,158,11,0.2)', padding: 35, display: 'flex', flexDirection: 'row', justifyContent: 'space-between' }}>
              <View style={{ flex: 1 }}>
                <Text style={{ color: '#FFF', fontSize: 32, fontWeight: '900', lineHeight: 40, marginBottom: 15, textShadowColor: '#F59E0B', textShadowOffset: {width:0, height:0}, textShadowRadius: 10 }}>Doctor{`\n`}Surgical Vault{`\n`}Vault</Text>
              </View>
              <img src={getUri(GoldShieldImg)} style={{ width: 140, height: 140, objectFit: 'contain', mixBlendMode: 'screen', animation: 'shieldFloat 4s ease-in-out infinite' }} />
            </div>
          </TouchableOpacity>
        </View>

        {/* ROW 2: Three Mini Cards */}
        <View style={{ flexDirection: 'row', gap: 20, height: 260 }}>
          {[
            { route: '/dashboard' as const, title: 'Clinic\nAnalytics', desc: 'Clinic ait accents in ruby red', color: '#F43F5E', glow: 'rgba(244,63,94,0.15)' },
            { route: '/dashboard' as const, title: 'Enter 5-Panel\nLab Vitals', desc: 'Enter 5-panel Lab vitals', color: '#10B981', glow: 'rgba(16,185,129,0.15)' },
            { route: '/register' as const, title: 'Register\nPatient', desc: 'Register your porrien cards', color: '#A855F7', glow: 'rgba(168,85,247,0.15)' },
          ].map((card) => (
            <TouchableOpacity key={card.title} style={{ flex: 1 }} onPress={() => router.push(card.route)}>
              <div style={{ flex: 1, height: '100%', background: `linear-gradient(180deg, ${card.glow} 0%, rgba(15,23,42,0.9) 100%)`, borderRadius: 20, borderWidth: 1.5, borderColor: card.color, padding: 30, display: 'flex', flexDirection: 'column', justifyContent: 'space-between', boxShadow: `0 0 30px ${card.glow}` }}>
                <View>
                  <Text style={{ color: '#FFF', fontSize: 26, fontWeight: '900', lineHeight: 32, marginBottom: 15, textShadowColor: card.color, textShadowOffset: {width:0,height:0}, textShadowRadius: 10 }}>{card.title}</Text>
                  <Text style={{ color: '#94A3B8', fontSize: 13, lineHeight: 20 }}>{card.desc}</Text>
                </View>
                
                {/* Custom Pill Toggle Bottom Right */}
                <div style={{ alignSelf: 'flex-end', width: 60, height: 32, borderRadius: 16, backgroundColor: 'rgba(0,0,0,0.5)', borderWidth: 1, borderColor: card.color, position: 'relative', display: 'flex', alignItems: 'center', boxShadow: `0 0 15px ${card.glow}, inset 0 0 10px ${card.glow}` }}>
                  <div style={{ width: 24, height: 24, borderRadius: 12, backgroundColor: '#FFF', position: 'absolute', right: 3, boxShadow: `0 0 10px ${card.color}` }} />
                </div>
              </div>
            </TouchableOpacity>
          ))}
        </View>

      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: { flexGrow: 1, backgroundColor: '#090E17', padding: 40, alignItems: 'center' }
});
"""

open('src/app/index.tsx', 'w', encoding='utf-8').write(index_content)
print("Updated explore.tsx and index.tsx")
