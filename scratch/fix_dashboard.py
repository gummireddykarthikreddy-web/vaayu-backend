import os

dashboard_content = """import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, Image, Dimensions } from 'react-native';
import { useRouter } from 'expo-router';

// USE PNGS NOW (Transparent)
const GlassCapsuleTube = require('../../assets/images/GlassCapsuleTube.png');

const getUri = (source: any): string => {
  if (!source) return '';
  if (typeof source === 'string') return source;
  if (typeof source === 'object') return source.uri || source.default || '';
  return String(source);
};

export default function Dashboard() {
  const router = useRouter();
  const [labData, setLabData] = useState<any>(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/labs/VAAYU-77572')
      .then(r => r.json())
      .then(data => setLabData(data))
      .catch(e => console.error(e));
  }, []);

  const bloodInventory = [
    { type: 'A+', count: 12, max: 20 },
    { type: 'A-', count: 4, max: 20 },
    { type: 'B+', count: 18, max: 20 },
    { type: 'B-', count: 2, max: 20 },
    { type: 'O+', count: 25, max: 30 },
    { type: 'O-', count: 8, max: 20 },
    { type: 'AB+', count: 6, max: 20 },
    { type: 'AB-', count: 1, max: 20 },
  ];

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <style>{`
        @keyframes liquidWave {
          0%, 100% { transform: translateY(0px) scaleY(1); }
          50% { transform: translateY(-3px) scaleY(1.02); }
        }
        @keyframes bubbleRise {
          0% { transform: translateY(0px) scale(0.8); opacity: 0.8; }
          100% { transform: translateY(-70px) scale(1.2); opacity: 0; }
        }
        .hud-border {
          border: 1px solid rgba(0,229,255,0.2);
          box-shadow: 0 0 20px rgba(0,0,0,0.5), inset 0 0 10px rgba(0,229,255,0.05);
        }
      `}</style>

      {/* HEADER ROW */}
      <View style={styles.hudHeaderRow}>
        <TouchableOpacity style={styles.backBtn} onPress={() => router.back()}>
          <Text style={styles.backBtnText}>← Back to Vaayu Hub</Text>
        </TouchableOpacity>
      </View>

      <View style={{ flexDirection: 'row', justifyContent: 'space-between', alignItems: 'flex-end', marginBottom: 20, width: '100%', maxWidth: 1400, alignSelf: 'center' }}>
        <Text style={styles.hudTitle}>CLINIC ANALYTICS DASHBOARD</Text>
        <TouchableOpacity style={styles.refreshBtn}>
          <Text style={styles.refreshBtnText}>↻ REFRESH</Text>
        </TouchableOpacity>
      </View>

      <View style={styles.mainGrid}>
        
        {/* LEFT COL: BLOOD INVENTORY */}
        <View style={styles.leftCol}>
          <div className="hud-border" style={{ flex: 1, backgroundColor: '#0A1220', borderRadius: 20, padding: 25, display: 'flex', flexDirection: 'column' }}>
            <Text style={styles.sectionHeader}>[ BLOOD INVENTORY ]</Text>
            
            <View style={styles.capsuleGrid}>
              {bloodInventory.map(item => {
                const fillPercent = Math.min(100, Math.max(15, (item.count / item.max) * 100));
                return (
                  <View key={item.type} style={styles.capsuleCell}>
                    
                    {/* The Capsule Itself */}
                    <View style={styles.capsuleTubeOuter}>
                      {/* Deep red liquid background fill that gets masked by the borderRadius */}
                      <div style={{ position: 'absolute', bottom: 0, left: 0, right: 0, height: `${fillPercent}%`, background: 'linear-gradient(180deg, #FF4D6D 0%, #9F1239 100%)' }}>
                        <div style={{ position: 'absolute', top: -4, left: 0, right: 0, height: 8, backgroundColor: '#FF8FA3', borderRadius: '50%', animation: 'liquidWave 3s ease-in-out infinite' }} />
                        {[0,1,2].map(bi => (
                          <div key={bi} style={{ position: 'absolute', bottom: `${10 + bi * 20}%`, left: `${20 + (bi * 20) % 50}%`, width: 4, height: 4, backgroundColor: 'rgba(255, 200, 220, 0.6)', borderRadius: '50%', animation: `bubbleRise ${2 + bi * 0.5}s infinite ${bi * 0.4}s` }} />
                        ))}
                      </div>
                      
                      {/* PNG Overlay to give the 3D Glass reflection */}
                      <img src={getUri(GlassCapsuleTube)} style={{ position: 'absolute', top: 0, left: 0, right: 0, bottom: 0, width: '100%', height: '100%', objectFit: 'contain', zIndex: 5, pointerEvents: 'none' }} />
                      
                      {/* Text in the middle */}
                      <View style={styles.capsuleTextOverlay}>
                        <Text style={styles.capsuleGroupText}>{item.type}</Text>
                        <Text style={styles.capsuleCountText}>{item.count} Units</Text>
                      </View>
                    </View>

                    {/* Progress Bar under the capsule */}
                    <View style={styles.capsuleProgressBarOuter}>
                      <div style={{ height: '100%', width: `${fillPercent}%`, backgroundColor: '#00E5FF', borderRadius: 2, boxShadow: '0 0 8px #00E5FF' }} />
                    </View>
                    <Text style={styles.capsulePercentText}>{Math.round(fillPercent)}%</Text>
                  </View>
                );
              })}
            </View>
          </div>
        </View>

        {/* RIGHT COL */}
        <View style={styles.rightCol}>
          
          {/* NEARBY BLOOD BANK DIRECTORY */}
          <div className="hud-border" style={{ backgroundColor: '#0A1220', borderRadius: 20, padding: 25, marginBottom: 20 }}>
            <Text style={styles.sectionHeader}>[ NEARBY BLOOD BANK DIRECTORY ]</Text>
            
            <View style={{ flexDirection: 'row', flexWrap: 'wrap', gap: 15 }}>
              {[
                { name: 'Red Cross Society Blood Bank', dist: '2.5 km away' },
                { name: 'Govt General Hospital Blood Bank', dist: '4 km away' },
                { name: 'Sanjeevani Lifeline Blood Bank', dist: '5.2 km away' },
                { name: 'Lions District Blood Center', dist: '7.1 km away' },
              ].map(bank => (
                <View key={bank.name} style={styles.bankCard}>
                  <Text style={styles.bankName}>{bank.name}</Text>
                  <Text style={styles.bankDist}>{bank.dist}</Text>
                  <Text style={styles.oneTapLabel}>[ 1-TAP CALL ]</Text>
                  <TouchableOpacity style={styles.callBtn}>
                    <div style={{ background: 'linear-gradient(180deg, #10B981 0%, #059669 100%)', borderRadius: 20, padding: '10px 0', textAlign: 'center', boxShadow: '0 4px 10px rgba(16,185,129,0.3)' }}>
                      <Text style={styles.callBtnText}>📞 CALL NOW</Text>
                    </div>
                  </TouchableOpacity>
                </View>
              ))}
            </View>
          </div>

          {/* LAB INPUT PODS */}
          <div className="hud-border" style={{ backgroundColor: '#0A1220', borderRadius: 20, padding: 25, flex: 1 }}>
            <Text style={styles.sectionHeader}>[ LAB INPUT PODS: PATIENT VITALS ]</Text>
            <View style={{ flexDirection: 'row', gap: 20, flex: 1 }}>
              <View style={{ flex: 1, backgroundColor: '#131C2D', borderRadius: 12, padding: 20, borderWidth: 1, borderColor: '#334155' }}>
                <Text style={{ color: '#E2E8F0', fontWeight: 'bold', marginBottom: 10 }}>[ PATIENT NAME: {(labData?.patient_name || 'ALISHA CHEN').toUpperCase()} ]</Text>
                <Text style={{ color: '#00E5FF', fontWeight: 'bold', marginBottom: 20 }}>1. [ ID: {labData?.patient_id || 'VAAYU-77572'} ]</Text>
                
                <Text style={{ color: '#E2E8F0', fontWeight: 'bold', marginBottom: 10 }}>2. [ TEMP: 98.6°F ]</Text>
                
                <View style={styles.ecgBox}>
                   {/* ECG sine wave mock */}
                   <svg width="100%" height="40" viewBox="0 0 100 40" preserveAspectRatio="none">
                     <polyline points="0,20 20,20 25,5 30,35 35,20 100,20" fill="none" stroke="#00E5FF" strokeWidth="2" strokeLinejoin="round" />
                   </svg>
                </View>
              </View>

              <View style={{ flex: 1, backgroundColor: '#131C2D', borderRadius: 12, padding: 20, borderWidth: 1, borderColor: '#334155' }}>
                <Text style={{ color: '#E2E8F0', fontWeight: 'bold', marginBottom: 20 }}>3. [ BLOOD PRESSURE: 120/80 ]</Text>
                <Text style={{ color: '#E2E8F0', fontWeight: 'bold', marginBottom: 20 }}>4. [ HEART RATE: 72 BPM ]</Text>
                <Text style={{ color: '#E2E8F0', fontWeight: 'bold', marginBottom: 20 }}>5. [ O2 SATURATION: 98% ]</Text>
              </View>
            </View>
          </div>

        </View>

      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: { flexGrow: 1, backgroundColor: '#050B14', padding: 30 },
  hudHeaderRow: { marginBottom: 10, width: '100%', maxWidth: 1400, alignSelf: 'center' },
  backBtn: { alignSelf: 'flex-start', paddingHorizontal: 15, paddingVertical: 8, backgroundColor: 'rgba(0, 229, 255, 0.1)', borderRadius: 8, borderWidth: 1, borderColor: '#00E5FF' },
  backBtnText: { color: '#00E5FF', fontWeight: 'bold', fontSize: 13 },
  
  hudTitle: { color: '#FFFFFF', fontSize: 26, fontWeight: '900', letterSpacing: 1.5, textShadowColor: '#FFFFFF', textShadowOffset: { width: 0, height: 0 }, textShadowRadius: 10 },
  refreshBtn: { paddingHorizontal: 15, paddingVertical: 8, borderRadius: 20, borderWidth: 1, borderColor: '#00E5FF', backgroundColor: 'rgba(0,229,255,0.05)' },
  refreshBtnText: { color: '#00E5FF', fontWeight: '900', fontSize: 12 },

  mainGrid: { maxWidth: 1400, width: '100%', alignSelf: 'center', flexDirection: 'row', gap: 20 },
  leftCol: { flex: 5 },
  rightCol: { flex: 4, display: 'flex', flexDirection: 'column' },
  
  sectionHeader: { color: '#FFFFFF', fontSize: 16, fontWeight: '900', letterSpacing: 1, marginBottom: 25 },
  
  capsuleGrid: { flexDirection: 'row', flexWrap: 'wrap', gap: 20, justifyContent: 'space-between', paddingHorizontal: 10 },
  capsuleCell: { width: '22%', minWidth: 90, alignItems: 'center', marginBottom: 30 },
  capsuleTubeOuter: { width: 60, height: 160, borderRadius: 30, overflow: 'hidden', backgroundColor: '#131C2D', position: 'relative', marginBottom: 15, borderWidth: 1, borderColor: 'rgba(255,255,255,0.1)' },
  capsuleTextOverlay: { position: 'absolute', top: 0, left: 0, right: 0, bottom: 0, justifyContent: 'center', alignItems: 'center', zIndex: 10 },
  capsuleGroupText: { color: '#FFFFFF', fontSize: 26, fontWeight: '900', textShadowColor: 'rgba(0,0,0,0.9)', textShadowOffset: { width: 0, height: 2 }, textShadowRadius: 6 },
  capsuleCountText: { color: '#FFFFFF', fontSize: 11, fontWeight: 'bold', marginTop: 2, textShadowColor: 'rgba(0,0,0,0.9)', textShadowOffset: { width: 0, height: 1 }, textShadowRadius: 3 },
  
  capsuleProgressBarOuter: { width: '80%', height: 4, backgroundColor: '#1E293B', borderRadius: 2, marginBottom: 8, overflow: 'hidden' },
  capsulePercentText: { color: '#00E5FF', fontSize: 12, fontWeight: 'bold' },

  bankCard: { width: '47%', backgroundColor: '#131C2D', borderRadius: 12, padding: 15, borderWidth: 1, borderColor: '#334155' },
  bankName: { color: '#FFFFFF', fontWeight: '900', fontSize: 13, marginBottom: 5 },
  bankDist: { color: '#94A3B8', fontSize: 11, marginBottom: 15 },
  oneTapLabel: { color: '#10B981', fontSize: 10, fontWeight: 'bold', marginBottom: 8 },
  callBtn: { width: '100%' },
  callBtnText: { color: '#FFFFFF', fontWeight: '900', fontSize: 12, textAlign: 'center' },

  ecgBox: { height: 80, backgroundColor: 'rgba(0,229,255,0.05)', borderWidth: 1, borderColor: '#00E5FF', borderRadius: 12, justifyContent: 'center', alignItems: 'center', marginTop: 15, overflow: 'hidden' }
});
"""

with open('src/app/dashboard.tsx', 'w', encoding='utf-8') as f:
    f.write(dashboard_content)

print("dashboard.tsx rewritten with UTF-8 encoding.")
