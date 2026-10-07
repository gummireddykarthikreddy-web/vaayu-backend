import '../polyfills';
import { Tabs } from 'expo-router';

export default function TabLayout() {
  return (
    <Tabs screenOptions={{ 
      headerShown: false, // This hides the black Expo Starter bar at the top!
      tabBarStyle: { display: 'none' } // This hides any default bottom tabs
    }}>
      <Tabs.Screen name="index" />
      <Tabs.Screen name="explore" />
    </Tabs>
  );
}
