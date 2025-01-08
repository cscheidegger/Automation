Feature: Frontend Automation Test
  As a QA engineer
  I want to test the Practice Form, Browser Windows, and Web Tables features
  So that I can validate their functionality

  Scenario: Fill out and submit the practice form
    Given I navigate to the Practice Form page
    When I fill out the form with random data
    And I upload a file
    And I submit the form
    Then I should see a success popup
    And I close the popup

 Scenario: Validate Browser Windows functionality
    Given I navigate to the Browser Windows page
    When I click the "New Window" button
    Then I should see a new window with the message "This is a sample page"
    And I close the new window

  Scenario: Web Tables - Basic record management
    Given I navigate to the Web Tables page
    When I add a new record
    Then I edit the last record
    And I delete the last record

  @dynamic
  Scenario: Web Tables - Dynamic records management
    Given I navigate to the Web Tables page
    When I create 12 new records dynamically
    Then I delete all records
 
 Scenario: Progress Bar functionality
    Given I navigate to the Progress Bar page
    When I start the progress bar
    And I wait for progress to reach 25 percent
    Then I verify the progress is not more than 25 percent
    And I reset the progress bar
    
  Scenario: Sort items in ascending order
    Given I navigate to the Sortable page
    When I sort the items in ascending order
    Then I should see the items sorted correctly