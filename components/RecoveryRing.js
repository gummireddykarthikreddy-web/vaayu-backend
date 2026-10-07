import { StyleSheet, Text, View } from 'react-native';
import Svg, { Circle } from 'react-native-svg';

export default function RecoveryRing({ score = 0 }) {
  // SVG and Circle math for the progress ring
  const radius = 50;
  const strokeWidth = 10;
  const circumference = 2 * Math.PI * radius;
  // Calculate how much of the ring to fill based on the score (0 to 100)
  const strokeDashoffset = circumference - (score / 100) * circumference;

  return (
    <View style={styles.container}>
      <Svg height="120" width="120" viewBox="0 0 120 120">
        {/* Background Track Circle */}
        <Circle
          cx="60"
          cy="60"
          r={radius}
          stroke="#E0E0E0"
          strokeWidth={strokeWidth}
          fill="none"
        />
        {/* Dynamic Progress Circle */}
        <Circle
          cx="60"
          cy="60"
          r={radius}
          stroke="#4CAF50" // Green color for recovery
          strokeWidth={strokeWidth}
          fill="none"
          strokeDasharray={circumference}
          strokeDashoffset={strokeDashoffset}
          strokeLinecap="round"
        />
      </Svg>
      {/* Display the score in the absolute center of the ring */}
      <Text style={styles.scoreText}>{score}%</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    justifyContent: 'center',
    alignItems: 'center',
    marginVertical: 20,
  },
  scoreText: {
    position: 'absolute',
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
  },
});