import axios from 'axios';
import { useRouter } from 'expo-router';
import { useState } from 'react';
import { Alert, ScrollView, StyleSheet, Text, TextInput, TouchableOpacity, View } from 'react-native';
import { API_BASE_URL } from '../constants/api';

export default function RegisterScreen() {
  const router = useRouter();
  const [form, setForm] = useState({
    full_name: '', date_of_birth: '', blood_group: '', 
    contact_number: '', emergency_contact: '',
    address: '', nearby_post_office: ''
  });
  const [loading, setLoading] = useState(false);

  const handleRegister = async () => {
    setLoading(true);
    try {
      const res = await axios.post(`${API_BASE_URL}/api/register`, form);
      if (res.data.status === 'success') {
        Alert.alert("Registration Complete", `Patient ID: ${res.data.patient_id}`);
        setForm({ full_name: '', date_of_birth: '', blood_group: '', contact_number: '', emergency_contact: '', address: '', nearby_post_office: '' });
      } else {
        Alert.alert("Error", res.data.message);
      }
    } catch(e) {
      Alert.alert("Error", "Could not connect to Vaayu backend.");
    }
    setLoading(false);
  };

  const renderInput = (key: keyof typeof form, label: string, placeholder: string) => (
    <View style={styles.hudPod}>
      <Text style={styles.podLabel}>[ {label.toUpperCase()} ]</Text>
      <TextInput
        style={styles.podInput}
        placeholder={placeholder}
        placeholderTextColor="#475569"
        value={form[key]}
        onChangeText={(text) => setForm({ ...form, [key]: text })}
      />
    </View>
  );

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <TouchableOpacity style={styles.backBtn} onPress={() => router.replace('/')}>
        <Text style={styles.backBtnText}>[ ← Back to Vaayu Hub ]</Text>
      </TouchableOpacity>

      <View style={styles.hudHeaderRow}>
        <Text style={styles.hudTitle}>PATIENT REGISTRATION HUD</Text>
        <Text style={styles.hudSubtitle}>SECURE ONBOARDING PROTOCOL</Text>
      </View>
      
      <View style={styles.bentoGrid}>
        {renderInput('full_name', 'Patient Full Name', 'e.g. Arjun Sharma')}
        {renderInput('date_of_birth', 'Date of Birth (YYYY-MM-DD)', '1988-05-14')}
        {renderInput('blood_group', 'Blood Group', 'e.g. O+, A-')}
        {renderInput('contact_number', 'Mobile Number', 'e.g. 9876543210')}
        {renderInput('emergency_contact', 'Emergency Contact', 'e.g. 9123456789')}
        {renderInput('address', 'Residential Address', 'H.No 4-12, Gandhi Nagar...')}
        {renderInput('nearby_post_office', 'Nearby Post Office & PIN', 'Guntur Head Post Office - 522002')}
      </View>

      <TouchableOpacity style={styles.submitBtn} onPress={handleRegister} disabled={loading}>
        <Text style={styles.submitBtnText}>{loading ? "INITIALIZING..." : "REGISTER PATIENT INTO VAAYU"}</Text>
      </TouchableOpacity>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: { flexGrow: 1, backgroundColor: '#050D1A', padding: 20 },
  backBtn: { alignSelf: 'flex-start', marginBottom: 20, padding: 10, backgroundColor: 'rgba(0, 229, 255, 0.1)', borderRadius: 8, borderWidth: 1, borderColor: '#00E5FF' },
  backBtnText: { color: '#00E5FF', fontWeight: 'bold' },
  hudHeaderRow: {
    marginBottom: 25, borderBottomWidth: 1, borderBottomColor: 'rgba(0, 229, 255, 0.2)', paddingBottom: 15, maxWidth: 1280, width: '100%', alignSelf: 'center',
  },
  hudTitle: { color: '#FFFFFF', fontSize: 24, fontWeight: '900', letterSpacing: 1.2, textShadowColor: 'rgba(0, 229, 255, 0.5)', textShadowOffset: {width: 0, height: 0}, textShadowRadius: 10 },
  hudSubtitle: { color: '#8892B0', fontSize: 12, fontWeight: 'bold', letterSpacing: 2, marginTop: 5 },
  
  bentoGrid: { maxWidth: 1280, width: '100%', alignSelf: 'center', flexDirection: 'row', flexWrap: 'wrap', gap: 20 },
  
  hudPod: {
    flex: 1, minWidth: 300, backgroundColor: '#0D1F3C', borderWidth: 1.5, borderColor: 'rgba(0, 229, 255, 0.35)',
    borderTopColor: 'rgba(255, 255, 255, 0.3)', borderRadius: 20, padding: 20,
    shadowColor: '#00E5FF', shadowOpacity: 0.25, shadowRadius: 18, elevation: 8,
  },
  podLabel: { color: '#00E5FF', fontSize: 12, fontWeight: 'bold', letterSpacing: 1.5, marginBottom: 12 },
  podInput: { backgroundColor: '#061224', borderWidth: 1, borderColor: '#00E5FF', borderRadius: 10, padding: 12, color: '#FFFFFF', fontSize: 15 },

  submitBtn: {
    maxWidth: 1280, width: '100%', alignSelf: 'center', backgroundColor: 'rgba(0, 255, 135, 0.15)',
    borderWidth: 1.5, borderColor: '#00FF87', padding: 18, borderRadius: 20, alignItems: 'center', marginTop: 30,
    shadowColor: '#00FF87', shadowOpacity: 0.4, shadowRadius: 15, elevation: 10,
  },
  submitBtnText: { color: '#00FF87', fontWeight: '900', fontSize: 16, letterSpacing: 1.5 }
});