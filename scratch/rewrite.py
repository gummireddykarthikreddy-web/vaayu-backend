import os

filepath = r"c:/Users/gummi/OneDrive/Documents/vaayu-patient-app/src/app/patient.tsx"

content = """import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, Image, TextInput, Alert, ActivityIndicator, ImageBackground } from 'react-native';
import { useRouter } from 'expo-router';
import AnimatedBlueFireOrb from '../components/AnimatedBlueFireOrb';

const GoldMicrochipImg = require('../../assets/images/GoldMicrochip.png');
const BurningBlueFireOrb = require('../../assets/images/BurningBlueFireOrb.jpg');
const GoldTreasureCard = require('../../assets/images/gold_treasure_card.jpg');

const getUri = (source: any): string => {
  if (!source) return '';
  if (typeof source === 'string') return source;
  if (typeof source === 'object') return source.uri || source.default || '';
  return String(source);
};

export default function PatientPortal() {
  const router = useRouter();
  const [patientData, setPatientData] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [deliveryAddress, setDeliveryAddress] = useState('');
  const [ordering, setOrdering] = useState(false);

  useEffect(() => {
    fetchPatientData();
  }, []);

  const fetchPatientData = async () => {
    setLoading(true);
    try {
      const res = await fetch('http://127.0.0.1:8000/patient/VHP-88390');
      if (!res.ok) throw new Error('Failed to fetch patient data');
      const data = await res.json();
      setPatientData(data);
      setDeliveryAddress(data.patient_info?.nearby_post_office || '');
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handlePlaceOrder = async () => {
    if (!deliveryAddress) {
      Alert.alert("Error", "Please provide a delivery address.");
      return;
    }
    setOrdering(true);
    try {
      const res = await fetch('http://127.0.0.1:8000/order-nutrimed', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ patient_id: patientData?.patient_info?.id || 'VHP-88390', delivery_address: deliveryAddress })
      });
      if (!res.ok) throw new Error('Failed to place order');
      const data = await res.json();
      Alert.alert("Success", data.message);
    } catch (err: any) {
      Alert.alert("Order Failed", err.message);
    } finally {
      setOrdering(false);
    }
  };

  const qrUrl = `https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=VHP-88390&color=0F172A&bgcolor=E2E8F0`;
  const latestLab = patientData?.lab_reports?.[0] || {};

  const recentLabRows = [
    { name: 'IRON LEVELS', value: latestLab.iron || 'HIGH', isNormal: false },
    { name: 'VITAMIN D', value: latestLab.vitamin_d || 'LOW', isNormal: false },
    { name: 'CHOLESTEROL', value: latestLab.cholesterol || 'NORMAL', isNormal: true },
    { name: 'HEMOGLOBIN', value: latestLab.hemoglobin || 'NORMAL', isNormal: true },
  ];

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <style>{`
        @keyframes fireSpin {
          0% { transform: rotate(0deg) scale(1); filter: brightness(1.2) contrast(1.3); }
          50% { transform: rotate(180deg) scale(1.05); filter: brightness(1.5) contrast(1.5); }
          100% { transform: rotate(360deg) scale(1); filter: brightness(1.2) contrast(1.3); }
        }
        @keyframes hoverTilt {
          0%, 100% { transform: perspective(1000px) rotateY(0deg) rotateX(0deg); }
          50% { transform: perspective(1000px) rotateY(4deg) rotateX(2deg); }
        }
      `}</style>
      
      <TouchableOpacity style={styles.backBtn} onPress={() => router.back()}>
        <Text style={styles.backBtnText}>← BACK TO HUB</Text>
      </TouchableOpacity>

      {loading && <ActivityIndicator size="large" color="#00E5FF" style={{ marginTop: 20 }} />}
      {error !== '' && <Text style={styles.errorText}>{error}</Text>}

      {patientData && !loading && (
        <View style={styles.mainGrid}>
          {/* ================= LEFT COLUMN ================= */}
          <View style={styles.leftCol}>
            
            {/* TOP: Vaayu Health Pass */}
            <View style={styles.standaloneCard}>
              <div style={{ background: 'linear-gradient(135deg, #F8FAFC 0%, #CBD5E1 50%, #94A3B8 100%)', borderTopLeftRadius: 16, borderTopRightRadius: 16, padding: 20 }}>
                <View style={{ flexDirection: 'row', justifyContent: 'space-between' }}>
                  <View style={{ flex: 1 }}>
                    <Text style={{ color: '#0F172A', fontSize: 22, fontWeight: '900', letterSpacing: -0.5 }}>Vaayu Health Pass</Text>
                    <Text style={{ color: '#475569', fontSize: 13, fontWeight: 'bold', marginBottom: 20 }}>Titanium Smart Card</Text>
                    <img src={getUri(GoldMicrochipImg)} style={{ width: 55, height: 40, borderRadius: 6, marginBottom: 20, objectFit: 'cover', boxShadow: '0 4px 6px rgba(0,0,0,0.3)' }} />
                    <Text style={[styles.hpCrispText, { color: '#0F172A' }]}>PATIENT: {(patientData.patient_info?.name || 'ANNA CHEN').toUpperCase()}</Text>
                    <Text style={[styles.hpCrispText, { color: '#0F172A' }]}>DOB: 12 OCT 1991</Text>
                    <Text style={[styles.hpCrispText, { color: '#0F172A' }]}>MEMBER ID: {patientData.patient_info?.id || 'VHP-88390'}</Text>
                    <Text style={[styles.hpCrispText, { color: '#059669', fontWeight: '900', marginTop: 5 }]}>STATUS: ACTIVE</Text>
                  </View>
                  <View style={{ alignItems: 'center', justifyContent: 'center' }}>
                    <div style={{ backgroundColor: '#E2E8F0', padding: 12, borderRadius: 16, boxShadow: 'inset 0 4px 8px rgba(255,255,255,0.8), 0 10px 20px rgba(0,0,0,0.4)' }}>
                      <Image source={{ uri: qrUrl }} style={{ width: 130, height: 130 }} />
                    </div>
                    <div style={{ width: 0, height: 0, borderLeft: '12px solid transparent', borderRight: '12px solid transparent', borderTop: '12px solid #E2E8F0', marginTop: -1 }} />
                  </View>
                </View>
              </div>
              
              <View style={[styles.hpBottomRow, { backgroundColor: '#1E293B', padding: 15, borderBottomLeftRadius: 16, borderBottomRightRadius: 16 }]}>
                <div style={{ flex: 1, height: 10, background: 'linear-gradient(90deg, #F59E0B 0%, #FDE047 60%, rgba(253,224,71,0) 100%)', borderRadius: 5, boxShadow: '0 0 12px rgba(245,158,11,0.5)' }} />
                <TouchableOpacity onPress={() => typeof window !== 'undefined' ? window.print() : Alert.alert('Print')} style={{ marginLeft: 20 }}>
                  <div style={{ background: 'linear-gradient(180deg, #E2E8F0 0%, #94A3B8 100%)', borderRadius: 6, padding: '10px 16px', boxShadow: '0 4px 10px rgba(0,0,0,0.4), inset 0 1px 2px #FFFFFF' }}>
                    <Text style={styles.printBtnText}>🖨️ PRINT PHYSICAL CARD</Text>
                  </div>
                </TouchableOpacity>
              </View>
            </View>

            {/* 11-Language AI Care Plan */}
            <View style={styles.standaloneCard}>
              <Text style={[styles.panelTitle, { color: '#FFFFFF' }]}>11-Language AI Care Plan</Text>
              
              <View style={styles.langGrid}>
                {[
                  { code: 'ENG', color: '#38BDF8' }, { code: 'ESP', color: '#F97316' }, { code: 'FRA', color: '#38BDF8' }, { code: 'DEU', color: '#FDE047' },
                  { code: 'RAT', color: '#4ADE80' }, { code: '中文', color: '#FDE047' }, { code: '日本語', color: '#E879F9' }, { code: '한국어', color: '#4ADE80' },
                  { code: 'العربية', color: '#4ADE80' }, { code: 'हिन्दी', color: '#F97316' }, { code: 'PYC', color: '#38BDF8' }, { code: 'POR', color: '#F97316' },
                ].map((lang) => (
                  <View key={lang.code} style={[styles.langPill3D, { borderColor: lang.color, boxShadow: `0 0 12px ${lang.color}40, inset 0 0 6px ${lang.color}30` }]}>
                    <Text style={{ color: lang.color, fontWeight: '900', fontSize: 13, letterSpacing: 1 }}>{lang.code}</Text>
                  </View>
                ))}
              </View>

              <View style={{ flexDirection: 'row', gap: 15, marginBottom: 15 }}>
                <View style={[styles.subCard, { flex: 1, flexDirection: 'row', alignItems: 'center' }]}>
                  <View style={[styles.iconBadge, { backgroundColor: '#F97316' }]}><Text style={{fontSize:16}}>🍴</Text></View>
                  <View>
                    <Text style={styles.subCardHeader}>DIET</Text>
                    <Text style={styles.bulletText}>VEGAN • HIGH PROTEIN</Text>
                  </View>
                </View>
                <View style={[styles.subCard, { flex: 1, flexDirection: 'row', alignItems: 'center' }]}>
                  <View style={[styles.iconBadge, { backgroundColor: '#10B981' }]}><Text style={{fontSize:16}}>🏃</Text></View>
                  <View>
                    <Text style={styles.subCardHeader}>EXERCISE</Text>
                    <Text style={styles.bulletText}>45 MIN CARDIO • 3X WEEK</Text>
                  </View>
                </View>
              </View>

              {/* Crimson Alert / Recent Labs Split */}
              <View style={{ flexDirection: 'row', gap: 15, alignItems: 'stretch' }}>
                <View style={[styles.hazardSection3D, { width: '42%', justifyContent: 'center', alignItems: 'center' }]}>
                  <Text style={{ fontSize: 24, marginBottom: 5 }}>⚠️</Text>
                  <Text style={{ color: '#FF2A5F', fontWeight: '900', fontSize: 15, textAlign: 'center', lineHeight: 22 }}>UPCOMING{`\n`}MEDICATION{`\n`}ALERT</Text>
                </View>
                
                <View style={[styles.subCard, { width: '55%' }]}>
                  <Text style={[styles.subCardHeader, { marginBottom: 10, fontSize: 11, color: '#94A3B8', letterSpacing: 1 }]}>RECENT LAB RESULTS</Text>
                  {recentLabRows.map((row, i) => (
                    <View key={i} style={styles.labRowCompact}>
                      <Text style={styles.labRowLabel} numberOfLines={1}>{row.name}</Text>
                      <Text style={{ color: row.isNormal ? '#4ADE80' : '#FF2A5F', fontSize: 11, fontWeight: 'bold' }}>
                        {row.isNormal ? 'NORMAL' : (row.value.includes('HIGH') ? 'HIGH' : 'LOW')}
                      </Text>
                      <Text style={{ color: row.isNormal ? '#4ADE80' : '#FF2A5F', marginLeft: 10 }}>{row.isNormal ? '✔' : '⚠️'}</Text>
                    </View>
                  ))}
                </View>
              </View>
            </View>
          </View>

          {/* ================= RIGHT COLUMN ================= */}
          <View style={styles.rightCol}>
            
            {/* TOP: Cellular Recovery Engine */}
            <View style={styles.standaloneCard}>
              <Text style={[styles.panelTitle, { color: '#FFFFFF' }]}>Cellular Recovery Engine</Text>
              
              <div style={{ position: 'relative', width: '100%', height: 280, display: 'flex', justifyContent: 'center', alignItems: 'center', marginBottom: 20 }}>
                {/* massive image to not clip flames, screen blend mode removes black background */}
                <img 
                  src={getUri(BurningBlueFireOrb)} 
                  style={{ position: 'absolute', width: 450, height: 450, top: -85, left: -65, objectFit: 'contain', mixBlendMode: 'screen', animation: 'fireSpin 12s linear infinite', pointerEvents: 'none' }} 
                />
                <AnimatedBlueFireOrb />
                
                <View style={[styles.orbTextLayer, { zIndex: 10 }]}>
                  <Text style={styles.orbPercent}>{patientData?.recovery_insights?.recovery_rate || 83.5}%</Text>
                  <Text style={styles.orbLabel}>RECOVERY</Text>
                </View>
              </div>

              {/* 4 Stats Grid */}
              <View style={styles.miniGrid}>
                {['HYDRATION STATUS', 'ENERGY LEVELS', 'MUSCLE TONE', 'IMMUNE RESPONSE'].map((label, idx) => {
                  const icons = ['💧', '⚡', '💪', '🛡️'];
                  const colors = ['#38BDF8', '#FDE047', '#F43F5E', '#10B981'];
                  const values = [88, 72, 91, 64];
                  return (
                    <View key={label} style={styles.miniPod}>
                      <View style={[styles.iconBox3D, { backgroundColor: colors[idx % 4] + '25' }]}>
                        <Text style={{ fontSize: 18 }}>{icons[idx % 4]}</Text>
                      </View>
                      <View>
                        <Text style={styles.miniLabel}>{label}</Text>
                        <Text style={styles.miniValue}>{values[idx]}%</Text>
                      </View>
                    </View>
                  );
                })}
              </View>
            </View>

            {/* NutriMed Delivery */}
            <View style={styles.standaloneCard}>
              <Text style={[styles.panelTitle, { color: '#FFFFFF', marginBottom: 15 }]}>Vaayu NutriMed Delivery</Text>
              
              <View style={{ flexDirection: 'row', gap: 15 }}>
                <View style={[styles.goldenBoxContainer, { width: '40%' }]}>
                  <ImageBackground source={getUri(GoldTreasureCard) as any} style={{ flex: 1, padding: 15, justifyContent: 'center' }} imageStyle={{ opacity: 0.8, borderRadius: 12 }}>
                    <Text style={styles.goldenTitle}>Golden{`\n`}Treasure Card</Text>
                    <Text style={styles.goldenSubtitle}>DELIVERY TRACKING</Text>
                  </ImageBackground>
                </View>

                <View style={{ flex: 1 }}>
                  <Text style={{ color: '#94A3B8', fontSize: 10, fontWeight: 'bold', marginBottom: 10, letterSpacing: 1 }}>MEAL SELECTOR TILES</Text>
                  <View style={{ flexDirection: 'row', gap: 10, marginBottom: 15 }}>
                    <View style={styles.mealTile}>
                      <View style={styles.mealCircle}><Text>🥗</Text></View>
                      <Text style={styles.mealTileTitle}>PROTEIN BOWL</Text>
                    </View>
                    <View style={styles.mealTile}>
                      <View style={styles.mealCircle}><Text>🥤</Text></View>
                      <Text style={styles.mealTileTitle}>SMOOTHIE PACK</Text>
                    </View>
                    <View style={styles.mealTile}>
                      <View style={styles.mealCircle}><Text>🥙</Text></View>
                      <Text style={styles.mealTileTitle}>DETOX SALAD</Text>
                    </View>
                  </View>
                  <View style={styles.controlRow}>
                    <View style={styles.navSquare}><Text style={{ color: '#FFF', fontWeight: 'bold' }}>{'<'}</Text></View>
                    <View style={styles.navSquare}><Text style={{ color: '#FFF', fontWeight: 'bold' }}>{'>'}</Text></View>
                    <TouchableOpacity style={{ flex: 1 }} onPress={handlePlaceOrder} disabled={ordering}>
                      <div style={{ background: 'linear-gradient(180deg, #10B981 0%, #059669 100%)', boxShadow: '0 0 15px rgba(16,185,129,0.5)', padding: '12px 20px', borderRadius: 8, textAlign: 'center' }}>
                        <Text style={[styles.emeraldBtnText, { textAlign: 'center' }]}>{ordering ? "..." : "PLACE ORDER"}</Text>
                      </div>
                    </TouchableOpacity>
                  </View>
                </View>
              </View>
            </View>

            {/* AI LAB ASSISTANT HAZARD MATRIX */}
            <View style={styles.standaloneCard}>
              <Text style={[styles.panelTitle, { color: '#FFFFFF', marginBottom: 15 }]}>AI LAB ASSISTANT HAZARD MATRIX</Text>
              
              <View style={styles.matrixTable}>
                {[
                  { param: 'IRON LEVELS', val: 'HIGH', hazard: true, action: 'ADJUST DIET', icon: '🍽️' },
                  { param: 'VITAMIN D', val: 'LOW', hazard: true, action: 'INCREASE SUNLIGHT', icon: '☀️' },
                  { param: 'CHOLESTEROL', val: 'NORMAL', hazard: false, action: 'MAINTAIN CURRENT REGIMEN', icon: '🏃' },
                  { param: 'CHOLESTEROL', val: 'NORMAL', hazard: false, action: 'MAINTAIN CURRENT REGIMEN', icon: '⏳' },
                  { param: 'IRON LEVELS', val: 'HIGH', hazard: false, action: 'ADJUST DIET', icon: '🖼️' },
                ].map((change, idx) => (
                  <View key={idx} style={styles.matrixRow}>
                    <View style={styles.matrixColLeft}>
                      <Text style={styles.matrixTextLeft}>{change.param} - {change.hazard ? <Text style={{color:'#FF2A5F'}}>{change.val}</Text> : <Text style={{color:'#4ADE80'}}>{change.val}</Text>}</Text>
                    </View>
                    <View style={styles.matrixColRight}>
                      <Text style={styles.matrixTextRight}>{change.icon}  {change.action}</Text>
                    </View>
                  </View>
                ))}
              </View>
            </View>

          </View>
        </View>
      )}
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: { flexGrow: 1, backgroundColor: '#09111E', padding: 30, paddingTop: 40 },
  backBtn: { alignSelf: 'flex-start', marginBottom: 20, padding: 10, backgroundColor: 'rgba(0, 229, 255, 0.1)', borderRadius: 8, borderWidth: 1, borderColor: '#00E5FF' },
  backBtnText: { color: '#00E5FF', fontWeight: 'bold' },
  errorText: { color: '#FF2A5F', textAlign: 'center', marginTop: 10, fontWeight: 'bold' },

  mainGrid: { maxWidth: 1200, width: '100%', alignSelf: 'center', flexDirection: 'row', justifyContent: 'space-between' },
  leftCol: { width: '48%', gap: 20 },
  rightCol: { width: '50%', gap: 20 },

  standaloneCard: { backgroundColor: '#131C2D', borderRadius: 20, padding: 22, borderWidth: 1, borderColor: 'rgba(255,255,255,0.05)', boxShadow: '0 8px 30px rgba(0,0,0,0.5)' } as any,
  panelTitle: { fontSize: 18, fontWeight: '900', letterSpacing: 0.5, marginBottom: 20 },
  
  hpCrispText: { fontSize: 11, fontWeight: '800', marginBottom: 5, letterSpacing: 0.5 },
  hpBottomRow: { flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', gap: 12 },
  printBtnText: { color: '#0F172A', fontWeight: '900', fontSize: 11, letterSpacing: 0.5 },

  langGrid: { flexDirection: 'row', flexWrap: 'wrap', width: '100%', gap: 12, marginBottom: 25 },
  langPill3D: { width: '22%', backgroundColor: '#0A101C', borderWidth: 2, paddingVertical: 10, borderRadius: 25, alignItems: 'center', justifyContent: 'center' } as any,
  subCard: { backgroundColor: '#1C2538', borderRadius: 12, padding: 15, borderWidth: 1, borderColor: '#334155' },
  iconBadge: { width: 32, height: 32, borderRadius: 8, justifyContent: 'center', alignItems: 'center', marginRight: 12 },
  subCardHeader: { color: '#FFFFFF', fontWeight: '900', fontSize: 14, letterSpacing: 1 },
  bulletText: { color: '#94A3B8', fontSize: 11, marginTop: 4, fontWeight: 'bold', letterSpacing: 0.5 },
  
  hazardSection3D: { borderWidth: 2, borderColor: '#FF2A5F', backgroundImage: 'linear-gradient(145deg, rgba(127,29,29,0.3), rgba(40,5,15,0.8))', padding: 15, borderRadius: 12, boxShadow: '0 0 20px rgba(255,42,95,0.3), inset 0 0 10px rgba(255,42,95,0.2)' } as any,
  labRowCompact: { flexDirection: 'row', justifyContent: 'space-between', marginBottom: 8, borderBottomWidth: 1, borderBottomColor: 'rgba(255,255,255,0.05)', paddingBottom: 8 },
  labRowLabel: { color: '#94A3B8', fontSize: 11, flex: 1, fontWeight: 'bold' },

  orbTextLayer: { position: 'absolute', justifyContent: 'center', alignItems: 'center' },
  orbPercent: { color: '#FFFFFF', fontSize: 44, fontWeight: '900', textShadowColor: '#00E5FF', textShadowOffset: { width: 0, height: 0 }, textShadowRadius: 20 },
  orbLabel: { color: '#E2E8F0', fontSize: 14, fontWeight: '900', letterSpacing: 2, marginTop: 5 },
  
  miniGrid: { flexDirection: 'row', flexWrap: 'wrap', gap: 15, justifyContent: 'space-between' },
  miniPod: { width: '47%', backgroundColor: '#1C2538', borderRadius: 12, padding: 12, flexDirection: 'row', alignItems: 'center', borderWidth: 1, borderColor: '#334155' },
  iconBox3D: { width: 32, height: 32, borderRadius: 8, justifyContent: 'center', alignItems: 'center', marginRight: 12 },
  miniLabel: { color: '#94A3B8', fontSize: 10, fontWeight: 'bold', marginBottom: 4 },
  miniValue: { color: '#FFFFFF', fontSize: 18, fontWeight: '900' },

  goldenBoxContainer: { borderRadius: 12, overflow: 'hidden', minHeight: 120 },
  goldenTitle: { color: '#FFFFFF', fontWeight: '900', fontSize: 16, textShadowColor: 'rgba(0,0,0,0.8)', textShadowOffset: { width: 0, height: 2 }, textShadowRadius: 4 },
  goldenSubtitle: { color: '#FDE047', fontSize: 10, marginTop: 6, fontWeight: 'bold', letterSpacing: 1 },
  mealTile: { flex: 1, backgroundColor: '#09111E', borderRadius: 12, borderWidth: 1, borderColor: '#334155', padding: 8, alignItems: 'center', justifyContent: 'center' },
  mealCircle: { width: 36, height: 36, borderRadius: 18, backgroundColor: '#1E293B', justifyContent: 'center', alignItems: 'center', marginBottom: 8 },
  mealTileTitle: { color: '#94A3B8', fontSize: 9, fontWeight: 'bold', textAlign: 'center', height: 24 },
  
  controlRow: { flexDirection: 'row', alignItems: 'center', gap: 10 },
  navSquare: { width: 44, height: 44, backgroundColor: '#1C2538', borderRadius: 10, justifyContent: 'center', alignItems: 'center', borderWidth: 1, borderColor: '#334155' },
  emeraldBtnText: { color: '#FFFFFF', fontWeight: '900', fontSize: 13, letterSpacing: 1 },

  matrixTable: { borderWidth: 1, borderColor: '#334155', borderRadius: 12, overflow: 'hidden' },
  matrixRow: { flexDirection: 'row', borderBottomWidth: 1, borderBottomColor: '#334155' },
  matrixColLeft: { flex: 1, padding: 12, backgroundColor: '#09111E', borderRightWidth: 1, borderRightColor: '#334155' },
  matrixColRight: { flex: 1.2, padding: 12, backgroundColor: '#131C2D' },
  matrixTextLeft: { color: '#94A3B8', fontSize: 11, fontWeight: 'bold', letterSpacing: 0.5 },
  matrixTextRight: { color: '#E2E8F0', fontSize: 11, fontWeight: 'bold', letterSpacing: 0.5 },
});
"""

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("Rewritten patient.tsx")
