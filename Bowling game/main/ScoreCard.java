package org.mvpigs.bowlingGame;

public class ScoreCard {
	
	private String scoreCard = "";
	private int totalScore = 0;
	private boolean firstRoll = true;
	private boolean spare = false;
	private boolean strike = false;
	private int firstRollPins = 0;
	private boolean doubleStrike = false;
	
	private int rolls = 0;
	
	public static String symbols = "-123456789X/";
	
	/* Constructores */
	
	public ScoreCard() {
		this.scoreCard = "";
		this.rolls = 0;
	}
	
	public ScoreCard(String scoreCard) {
		this.scoreCard = scoreCard;
		this.rolls = scoreCard.length();
	}
	
	/* getters y setters */
	
	public String getScoreCard(){
		return this.scoreCard;
	}
	
	public int getTotalScore() {
		return this.totalScore;
	}

	private void setTotalScore(int total) {
		this.totalScore = total;
	}
		
	private boolean isSpare(){
		return this.spare;
	}
	
	private void setSpare(boolean spare){
		this.spare = spare;
	}
	
	private boolean isFirstRoll(){
		return this.firstRoll;
	}
	
	private void setFirstRoll(boolean value){
		this.firstRoll = value;
	}