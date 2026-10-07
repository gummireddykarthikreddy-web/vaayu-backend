import os

code = """import React from 'react';
import { ScrollView, TouchableOpacity } from 'react-native';
import { useRouter } from 'expo-router';

const HologramAvatarImg = require('../../assets/images/HologramAvatar.png');
const GoldShieldImg = require('../../assets/images/GoldShield.png');

const getUri = (source: any): string => {
  if (!source) return '';
  if (typeof source === 'string') return source;
  if (typeof source === 'object') return source.uri || source.default || '';
  return String(source);
};

export default function IndexHub() {
  const router = useRouter();

  return (
    <ScrollView contentContainerStyle={{ flexGrow: 1, backgroundColor: '#050B14', padding: 40, alignItems: 'center' }}>
      <style>{`
        * { box-sizing: border-box; }
        @keyframes floatHover {
          0%, 100% { transform: translateY(0px); }
          50% { transform: translateY(-15px); }
        }
        .hero-banner {
          background: linear-gradient(90deg, rgba(30,41,59,0.7), rgba(15,23,42,0.9));
          border: 1px solid rgba(255,255,255,0.15);
          box-shadow: 0 10px 30px rgba(0,0,0,0.8), inset 0 2px 10px rgba(255,255,255,0.05);
          backdrop-filter: blur(10px);
        }
        .slab-cyan {
          background: linear-gradient(135deg, rgba(56,189,248,0.25) 0%, rgba(15,23,42,0.9) 100%);
          border: 1px solid rgba(56,189,248,0.3);
          border-bottom: 14px solid rgba(148,163,184,0.35);
          box-shadow: 0 20px 40px rgba(0,0,0,0.6), inset 0 2px 20px rgba(56,189,248,0.2);
          backdrop-filter: blur(20px);
        }
        .slab-plat {
          background: linear-gradient(135deg, rgba(148,163,184,0.35) 0%, rgba(30,41,59,0.85) 100%);
          border: 1px solid rgba(245,158,11,0.3);
          border-bottom: 14px solid rgba(148,163,184,0.35);
          box-shadow: 0 20px 40px rgba(0,0,0,0.6), inset 0 2px 20px rgba(245,158,11,0.15);
          backdrop-filter: blur(20px);
        }
        .mini-card {
          border-radius: 20px;
          border-width: 2px;
          border-style: solid;
          padding: 25px;
          display: flex;
          flex-direction: column;
          justify-content: space-between;
          height: 250px;
          flex: 1;
        }
        .pill-toggle {
          width: 50px; height: 26px; border-radius: 13px; background: rgba(0,0,0,0.5); border: 2px solid; position: relative;
          box-shadow: inset 0 0 8px rgba(0,0,0,0.8);
        }
        .pill-knob {
          width: 20px; height: 20px; border-radius: 10px; background: #FFF; position: absolute; top: 1px; right: 2px;
          box-shadow: 0 2px 5px rgba(0,0,0,0.5);
        }
      `}</style>

      <div style={{ width: '100%', maxWidth: 1200, display: 'flex', flexDirection: 'column', gap: 30 }}>
        
        {/* TOP BANNER */}
        <div className="hero-banner" style={{ width: '100%', borderRadius: 18, padding: '25px 40px', textAlign: 'center' }}>
          <h1 style={{ margin: 0, color: '#FFF', fontSize: 32, fontWeight: '900', letterSpacing: 0.5, lineHeight: 1.3 }}>
            Welcome to Vaayu — National 3D Cellular<br/>Recovery & Surgical Ecosystem
          </h1>
        </div>

        {/* ROW 1: Massive 3D Glass Slabs */}
        <div style={{ display: 'flex', flexDirection: 'row', gap: 30, height: 290 }}>
          
          <TouchableOpacity style={{ flex: 1 }} onPress={() => router.push('/patient')}>
            <div className="slab-cyan" style={{ width: '100%', height: '100%', borderRadius: 24, padding: 35, display: 'flex', flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' }}>
              <div style={{ flex: 1 }}>
                <h2 style={{ margin: 0, color: '#FFF', fontSize: 34, fontWeight: '900', lineHeight: 1.2, textShadow: '0 0 15px #38BDF8', marginBottom: 15 }}>
                  Vaayu Patient<br/>Portal &<br/>NutriMed
                </h2>
                <p style={{ margin: 0, color: '#94A3B8', fontSize: 16 }}>3D hologram hologram</p>
              </div>
              <img src={getUri(HologramAvatarImg)} style={{ width: 160, height: 160, objectFit: 'contain', animation: 'floatHover 4s ease-in-out infinite' }} />
            </div>
          </TouchableOpacity>

          <TouchableOpacity style={{ flex: 1 }} onPress={() => router.push('/explore')}>
            <div className="slab-plat" style={{ width: '100%', height: '100%', borderRadius: 24, padding: 35, display: 'flex', flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' }}>
              <div style={{ flex: 1 }}>
                <h2 style={{ margin: 0, color: '#FFF', fontSize: 34, fontWeight: '900', lineHeight: 1.2, textShadow: '0 0 15px #F59E0B', marginBottom: 15 }}>
                  Doctor<br/>Surgical Vault<br/>Vault
                </h2>
              </div>
              <div style={{ position: 'relative', width: 160, height: 160, display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
                <div style={{ position: 'absolute', width: 100, height: 100, background: 'radial-gradient(circle, rgba(245,158,11,0.6) 0%, rgba(245,158,11,0) 70%)', filter: 'blur(10px)' }} />
                <img src={getUri(GoldShieldImg)} style={{ width: 140, height: 140, objectFit: 'contain', animation: 'floatHover 4s ease-in-out infinite 1s', zIndex: 2 }} />
              </div>
            </div>
          </TouchableOpacity>

        </div>

        {/* ROW 2: 3 Vertical Cards */}
        <div style={{ display: 'flex', flexDirection: 'row', gap: 30 }}>
          
          <TouchableOpacity style={{ flex: 1 }} onPress={() => router.push('/dashboard')}>
            <div className="mini-card" style={{ background: 'linear-gradient(180deg, rgba(244,63,94,0.15) 0%, rgba(15,23,42,0.9) 100%)', borderColor: '#F43F5E', boxShadow: '0 0 30px rgba(244,63,94,0.15)' }}>
              <div>
                <h3 style={{ margin: 0, color: '#FFF', fontSize: 28, fontWeight: '900', lineHeight: 1.2, textShadow: '0 0 15px #F43F5E', marginBottom: 10 }}>Clinic<br/>Analytics</h3>
                <p style={{ margin: 0, color: '#94A3B8', fontSize: 14 }}>Clinic ait accents in ruby red</p>
              </div>
              <div style={{ alignSelf: 'flex-end', display: 'flex', alignItems: 'flex-end' }}>
                <div className="pill-toggle" style={{ borderColor: '#F43F5E', boxShadow: '0 0 15px rgba(244,63,94,0.5)' }}>
                  <div className="pill-knob" style={{ boxShadow: '0 0 10px #F43F5E' }} />
                </div>
              </div>
            </div>
          </TouchableOpacity>

          <TouchableOpacity style={{ flex: 1 }} onPress={() => router.push('/dashboard')}>
            <div className="mini-card" style={{ background: 'linear-gradient(180deg, rgba(16,185,129,0.15) 0%, rgba(15,23,42,0.9) 100%)', borderColor: '#10B981', boxShadow: '0 0 30px rgba(16,185,129,0.15)' }}>
              <div>
                <h3 style={{ margin: 0, color: '#FFF', fontSize: 28, fontWeight: '900', lineHeight: 1.2, textShadow: '0 0 15px #10B981', marginBottom: 10 }}>Enter 5-Panel<br/>Lab Vitals</h3>
                <p style={{ margin: 0, color: '#94A3B8', fontSize: 14 }}>Enter 5-panel Lab vitals</p>
              </div>
              <div style={{ alignSelf: 'flex-end', display: 'flex', alignItems: 'flex-end' }}>
                <div className="pill-toggle" style={{ borderColor: '#10B981', boxShadow: '0 0 15px rgba(16,185,129,0.5)' }}>
                  <div className="pill-knob" style={{ boxShadow: '0 0 10px #10B981' }} />
                </div>
              </div>
            </div>
          </TouchableOpacity>

          <TouchableOpacity style={{ flex: 1 }} onPress={() => router.push('/register')}>
            <div className="mini-card" style={{ background: 'linear-gradient(180deg, rgba(168,85,247,0.15) 0%, rgba(15,23,42,0.9) 100%)', borderColor: '#A855F7', boxShadow: '0 0 30px rgba(168,85,247,0.15)' }}>
              <div>
                <h3 style={{ margin: 0, color: '#FFF', fontSize: 28, fontWeight: '900', lineHeight: 1.2, textShadow: '0 0 15px #A855F7', marginBottom: 10 }}>Register<br/>Patient</h3>
                <p style={{ margin: 0, color: '#94A3B8', fontSize: 14 }}>Register your porrien cards</p>
              </div>
              <div style={{ alignSelf: 'flex-end', display: 'flex', alignItems: 'flex-end' }}>
                <div className="pill-toggle" style={{ borderColor: '#A855F7', boxShadow: '0 0 15px rgba(168,85,247,0.5)' }}>
                  <div className="pill-knob" style={{ boxShadow: '0 0 10px #A855F7' }} />
                </div>
              </div>
            </div>
          </TouchableOpacity>

        </div>
      </div>
    </ScrollView>
  );
}
"""
with open('src/app/index.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print("index.tsx written")
