import androidx.test.ext.junit.rules.ActivityScenarioRule;
import androidx.test.ext.junit.runners.AndroidJUnit4;
import androidx.test.espresso.Espresso;
import static androidx.test.espresso.assertion.ViewAssertions.matches;
import static androidx.test.espresso.matcher.ViewMatchers.withId;
import static androidx.test.espresso.matcher.ViewMatchers.withText;
import static androidx.test.espresso.Espresso.onView;
import static androidx.test.espresso.action.ViewActions.click;

import org.junit.Rule;
import org.junit.Test;
import org.junit.runner.RunWith;

@RunWith(AndroidJUnit4.class)
public class MainActivityUITest {

    @Rule
    public ActivityScenarioRule<MainActivity> activityRule = new ActivityScenarioRule<>(MainActivity.class);

    @Test
    public void testButtonClick_updatesTextView() {
        // Simulieren eines Klicks auf den Button
        onView(withId(R.id.btnClickMe)).perform(click());

        // Überprüfen, ob der Text des TextViews geändert wurde
        onView(withId(R.id.txtViewResult)).check(matches(withText("Button geklickt")));
    }

    // Weitere UI-Tests für andere Aktivitäten und Interaktionen
}
